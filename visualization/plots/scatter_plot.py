import matplotlib  # These two lines are only needed
matplotlib.use('Agg')  # if you are running this via ssh
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os.path

filename = sys.argv[1]

fig, ax = plt.subplots()

data = np.loadtxt(filename)

x = data[:,0]
y = data[:,1]
z = data[:,2]

ax.patch.set_facecolor('black')
ax.set_xlim(-100,600)
ax.set_ylim(-100,600)

ax.scatter(x,y, color='r', s=2, marker='.', alpha=0.25)

plt.savefig(filename + '_1000_100data2.png',dpi=300)
#plt.show()
