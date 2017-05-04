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

if len(sys.argv) == 7:		#conditional check for requisite number
	filename = sys.argv[1]  #of arguments at run time
	N = sys.argv[2]
	D = sys.argv[3]
	S = sys.argv[4]
	G = sys.argv[5]
	dt = sys.argv[6]
else:
	print '\nThe proper use of gravsim.py is as follows.'
	print '\npython gravsim.py outputfile N D S G dt\n'
	print 'Where N is the number of particles'
	print 'D is the number of dimensions, S is the'
	print 'number of steps, G is the gravitational constant'
	print 'and dt is the time step\n'

	sys.exit(2)
for i in range(5):
	i = 2
	test = sys.argv[i]
	if test.isdigit():	#conditional check for integer values of
		continue	#N, D, and S
	else:
		print '\nN, D, and S must be integers\n'
		sys.exit(2)

#####################################################################
#Simulate function from Computation book modified to take in	    #
#user specified variables N, D, S, G, dt and output a user specified#
#file name.							    #
#####################################################################
def simulate(N, D, S, G, dt):
        x0, v0, m = book.initial_cond(N, D)
        for s in range(S):
                with open(filename + str(s+1) +".dat", "w") as myfile:
                        x1, v1 = book.timestep(x0, v0, G, m, dt)
                        x0, v0 = x1, v1
                        for n in range(N):
				 myfile.write(str(x0[n,0]) + "  "
					 + str(x0[n,1]) + "  " + str(x0[n,2]) + "\n")
                        myfile.flush()


#simulate(1000, 3, 1, 1.0, 1.0e-3)
simulate(int(N), int(D), int(S), float(G), float(dt))
print '\nSimulation complete. Your data has been saved as ' + sys.argv[1] + '*.dat\n'

#####################################################################
#								    #
#	Animation Section					    #
#								    #
#								    #
#####################################################################

fig, ax = plt.subplots()
x, y, z = np.loadtxt(filename + "1.dat", delimiter='  ', unpack=True)

line, = ax.plot(x, y, 'yo')
ax.set_xlim(-2000,2000)
ax.set_ylim(-2000,2000)
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
