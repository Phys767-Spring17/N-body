#import matplotlib  # These two lines are only needed
#matplotlib.use('Agg')  # if you are running this via ssh

import sys  # modules used to fancify user interface.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


filename = sys.argv[1]  # root of file names to be animated.
S = sys.argv[2]  # number of time steps to be animated.

fig, ax = plt.subplots()

x, y, z = np.loadtxt(filename + "1.dat", delimiter=' ', unpack=True)

line, = ax.plot(x, y, 'yo')

ax.set_xlim(-1000,1000)
ax.set_ylim(-1000,1000)


def animate(i):
    x, y, z = np.loadtxt(filename + str(i+1) + ".data", delimiter='  ', unpack=True)
    plt.title("Time " + str(i))
    line.set_data(x, y)
    return line, 


def init():
    """Init only required for blitting to give a clean slate.
    
    """
    line.set_ydata(np.ma.array(x, mask=True))
    return line,


ani = animation.FuncAnimation(fig, animate, np.arange(1, int(S)), init_func=init,
                              interval=25, blit=True)
#plt.show()
ani.save(filename + '.mp4')
