#http://stackoverflow.com/questions/2369492/generate-a-heatmap-in-matplotlib-using-a-scatter-data-set

import numpy as np
import matplotlib.pyplot as plt
import sphviewer as sph


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


fig = plt.figure()
ax1 = fig.add_subplot(111)

x, y, z = np.loadtxt('proctemp1000.data', delimiter=' ', unpack=True)

ax1.set_xlim(-100,600)
ax1.set_ylim(-100,600)

heatmap_1024, extent_1024 = myplot(x, y, nb=1024)

cax = ax1.imshow(heatmap_1024, extent=extent_1024, origin='lower', aspect='auto', cmap='gist_heat')
ax1.set_title("Smoothing over 1024 neighbors")
plt.colorbar(cax, ticks=[0.00, 0.25, 0.50, 0.75, 1.00])

plt.show()

plt.savefig('heat_1000_100.png', dpi=300)
