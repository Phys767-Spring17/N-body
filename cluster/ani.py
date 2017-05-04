# -*- coding: utf-8 -*-
#!/usr/bin/python   ##Shabang!

#############################################################################################################
#													    #
#    Written by:											    #
#													    #
#  '*¨'`·- .,  ‘                       ,.,   '            ,.-.                                 _,.,,_       # 
# \`:·-,. ,   '` ·.  '               ;´   '· .,          /   ';\ '                        ,.·'´  ,. ,  `;\ '#
#  '\:/   ;\:'`:·,  '`·, '         .´  .-,    ';\       ';    ;:'\      ,·'´';          .´   ;´:::::\`´ \'\ #
#   ;   ;'::\;::::';   ;\         /   /:\:';   ;:'\'    ';   ;::;     ,'  ,' '\       /   ,'::\::::::\:::\:'#
#   ;  ,':::;  `·:;;  ,':'\'     ,'  ,'::::'\';  ;::';  ';   ';::;   ,'  ,':::'\'    ;   ;:;:-·'~^ª*';\'´   #
#  ;   ;:::;    ,·' ,·':::; ,.-·'  '·~^*'´¨,  ';::;     ';   ;:;  ,'  ,':::::;'     ;  ,.-·:*'´¨'`*´\::\ '  #
#  ;  ;:::;'  ,.'´,·´:::::; ':,  ,·:²*´¨¯'`;  ;::';      ;   ;:;'´ ,'::::::;'  '   ;   ;\::::::::::::'\;'   #
# ':,·:;::-·´,.·´\:::::;´'  ,'  / \::::::::';  ;::';    ';   '´ ,·':::::;'        ;   ;'_\_:;:: -·^*';\     #
#  \::;. -·´:::::;\;·´    ,' ,'::::\·²*'´¨¯':,'\:;       ,'   ,.'\::;·´         ';    ,  ,. -·:*'´:\:'\     #
#   \;'\::::::::;·´'       \`¨\:::/          \::\'        \`*´\:::\;     ‘        \`*´ ¯\:::::::::::\;' '   #
#      `\;::-·´            '\::\;'            '\;'  '       '\:::\;'               \:::::\;::-·^*'´         #
#                            `¨'                            `*´‘                     `*´¯                   #
# Very obnoxious mode: Active										    #
#############################################################################################################

import matplotlib		#These two lines are only needed
matplotlib.use('Agg')		#if you are running this via ssh

import bookLimit as book#functions taken from book packaged as a module.
import sys, getopt	#modules used to fancify user interface.
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

#####################################################################						    
#run time argument handeling of user defined values.		    #
#						    		    #
#####################################################################

#if len(sys.argv) == 2:		#conditional check for requisite number
filename = sys.argv[1]  #of arguments at run time
S = sys.argv[2]
#else:
#	print '\nThe proper use of gravsim.py is as follows.'
#	print '\npython gravsim.py outputfile N D S G dt\n'
#	print 'Where N is the number of particles'
#	print 'D is the number of dimensions, S is the'
#	print 'number of steps, G is the gravitational constant'
#	print 'and dt is the time step\n'
#
#	sys.exit(2)

#####################################################################
#Simulate function from Computation book modified to take in	    #
#user specified variables N, D, S, G, dt and output a user specified#
#file name.							    #
#####################################################################

#####################################################################
#								    #
#	Animation Section					    #
#								    #
#								    #
#####################################################################

fig, ax = plt.subplots()
x, y, z = np.loadtxt(filename + "1.dat", delimiter='  ', unpack=True)

line, = ax.plot(x, y, 'yo')
ax.set_xlim(-1000,1000)
ax.set_ylim(-1000,1000)
#ax.set_facecolor('black')


def animate(i):
    x, y, z = np.loadtxt(filename + str(i+1) + ".dat", delimiter='  ', unpack=True)
#    line.set_label("test" + str(i) )
    plt.title("Time " + str(i))
    line.set_data(x, y)
    return line, 

# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, int(S)), init_func=init,
                              interval=25, blit=True)

ani.save(filename + '.mp4')

#choice = input('Would you like to save your output as an mp4?  yes = 1 no =/= 1' )
#if choice = 1:
#	ani.save('gravAni2.mp4')
#else:
#	plt.show()
