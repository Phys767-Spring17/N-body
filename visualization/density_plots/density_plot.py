# http://stackoverflow.com/questions/2369492/generate-a-heatmap-in-matplotlib-using-a-scatter-data-set
import matplotlib  # These two lines are only needed
matplotlib.use('Agg')  # if you are running this via ssh

import numpy as np
import matplotlib.pyplot as plt
import sphviewer as sph
import sys


def myplot(x, y, nb=32, xsize=500, ysize=500):   
    """This function reads in a set of data and smooths it using
       nearest neighbors summing. It then outputs the smoothed data
       with a measure of its extent. This output is then inputed to
       Axes.imshow.
       
       :param: x,y   two columns of data such as particle positions
       :param: nb    smoothing size.
    """
    xmin = np.min(x)
    xmax = np.max(x)
    ymin = np.min(y)
    ymax = np.max(y)

    x0 = (xmin+xmax)/2.
    y0 = (ymin+ymax)/2.

    pos = np.zeros([3, len(x)])
    pos[0, :] = x
    pos[1, :] = y
    w = np.ones(len(x))

    P = sph.Particles(pos, w, nb=nb)
    S = sph.Scene(P)
    S.update_camera(r='infinity', x=x0, y=y0, z=0, 
                    xsize=xsize, ysize=ysize)
    R = sph.Render(S)
    R.set_logscale()
    img = R.get_image()
    extent = R.get_extent()
    for i, j in zip(xrange(4), [x0,x0,y0,y0]):
        extent[i] += j
    print extent, x0, y0
    return img, extent


filename = sys.argv[1]

fig = plt.figure()
ax1 = fig.add_subplot(111)

data = np.loadtxt(filename)

x = data[:,0]
y = data[:,1]
z = data[:,2]

nb_val=2048

ax1.set_xlim(-100,600)
ax1.set_ylim(-100,600)

ax1.tick_params(axis='x', labelsize=6)
ax1.tick_params(axis='y', labelsize=6)

densitymap, extent = myplot(x, y, nb=nb_val)

cax = ax1.imshow(densitymap, extent=extent, origin='lower', aspect='auto', cmap='viridis')
ax1.set_title("100 Clusters of 1000 particles \n Smoothing over "+ str(nb_val) +" neighbors", fontsize=10)

cbar = plt.colorbar(cax)
cbar.set_label('density of particles', labelpad=5, y=0.5, fontsize=8)
cbar.ax.tick_params(labelsize=6)

plt.xlabel("x position", fontsize=8)
plt.ylabel("y position", fontsize=8)

plt.savefig('density_' + str(nb_val) + '_1000_100.png', dpi=300)
