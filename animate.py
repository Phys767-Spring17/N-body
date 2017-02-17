

#import matplotlib		#These two lines are only needed
#matplotlib.use('Agg')		#if you are running this via ssh
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

fig, ax = plt.subplots()
x, y, z = np.loadtxt("new1.dat", delimiter='  ', unpack=True)

line, = ax.plot(x, y, 'yo')
ax.set_xlim(-1004,-994)
ax.set_ylim(-1004,-994)
#ax.set_facecolor('black')


def animate(i):
    x, y, z = np.loadtxt("new" + str(i+1) + ".dat", delimiter='  ', unpack=True)
    line.set_label("test" + str(i) )
    plt.title("Time " + str(i))
    line.set_data(x, y)
    return line, 



# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 3000), init_func=init,
                              interval=25, blit=True)



ani.save('gravsym1.mp4')
#plt.show()
