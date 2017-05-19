import matplotlib		#These two lines are only needed
matplotlib.use('Agg')		#if you are running this via ssh
import sys, getopt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os.path

fig, ax = plt.subplots()

x, y, z = np.loadtxt('temp1000.data', delimiter=' ', unpack=True)

line, = ax.plot(x, y, 'r.', markersize=2, alpha='0.25')
ax.patch.set_facecolor('black')
ax.set_xlim(-100,600)
ax.set_ylim(-100,600)

#plt.show()

plt.savefig('1000_100data2.png',dpi=1000)
