# -*- coding: utf-8 -*-
#!/usr/bin/python   ##Shabang!

########################################################################################################
#												       #
#    Written by:										       #
#												       #
#   '*¨'`·- .,  ‘                       ,.,   '         ,.-.                              _,.,         #
#  \`:·-,. ,   '` ·.  '               ;´   '· .,       /   ';\ '                     ,.·'´  ,. ,  `;\ '#
# '\:/   ;\:'`:·,  '`·, '          .´  .-,    ';\    ';    ;:'\      ,·'´';       .´   ;´:::::\`'´ \'\ #
#  ;   ;'::\;::::';   ;\         /   /:\:';   ;:'\'   ';   ;::;     ,'  ,''\     /   ,'::\::::::\:::\:'#
#  ;  ,':::;  `·:;;  ,':'\'     ,'  ,'::::'\';  ;::'; ';   ';::;   ,'  ,':::'\' ;   ;:;:-·'~^ª*';\'´   #  
# ;   ;:::;    ,·' ,·':::; ,.-·'  '·~^*'´¨,  ';::;    ';   ;:;  ,'  ,':::::;'  ;  ,.-·:*'´¨'`*´\::\ '  #
# ;  ;:::;'  ,.'´,·´:::::; ':,  ,·:²*´¨¯'`;  ;::';     ;   ;:;'´ ,'::::::;' ' ;   ;\::::::::::::'\;'   #
#':,·:;::-·´,.·´\:::::;´'  ,'  / \::::::::';  ;::';    ';   '´ ,·':::::;'     ;  ;'_\_:;:: -·^*';\     #
# \::;. -·´:::::;\;·´    ,' ,'::::\·²*'´¨¯':,'\:;      ,'   ,.'\::;·´       ';    ,  ,. -·:*'´:\:'\    #
#  \;'\::::::::;·´'       \`¨\:::/          \::\'       \`*´\:::\;     ‘     \`*´ ¯\:::::::::::\;' '   #
#     `\;::-·´            '\::\;'            '\;'  '    '\:::\;'              \:::::\;::-·^*'´         #
#                           `¨'                           `*´‘                 `*´¯                    #
#very obnoxious mode: Active									       #
########################################################################################################


import book	#functions taken from book packaged as a module.
import sys, getopt	#modules used to fancify user interface.

#####################################################################						    
#run time argument handeling of user defined values.		    #
#						    		    #
#####################################################################


def input_check(n):
    """run time argument handeling of user defined values.
    A total of 7 arguments must be included at run time
    as defined by the error message listed below.

    filename: The output filename.
    N: The number of particles in the simulation.
    D: The number of dimensions.
    S: The number of time steps to be used for the simulation.
    G: Gravitational constant.
    dt: the time step interval.
    """
    if len(sys.argv) == 7:
        filename = sys.argv[1]  #of arguments at run time
        N = sys.argv[2]
        D = sys.argv[3]
        S = sys.argv[4]
        G = sys.argv[5]
        dt = sys.argv[6]
        return filename, N, D, S, G, dt
    else:
        print '\nThe proper use of gravsim.py is as follows.'
        print '\npython gravsim.py outputfile N D S G dt\n'
        return sys.exit(2)
    

def input_int_check(N, D, S):
    """conditional check for integer values of N, D, and S.
    
    N: The number of particles in the simulation.
    D: The number of dimensions.
    S: The number of time steps to be used for the simulation.  
    """
    for i in range(5):
        i = 2
        test = sys.argv[i]
        if test.isdigit():
            continue
        else:
            print '\nN, D, and S must be integers\n'
            sys.exit(2)


#filename, N, D, S, G, dt = input_check(sys.argv)
#input_int_check(N, D, S)

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
    return '\nSimulation complete. Your data has been saved as ' + sys.argv[1] + '*.dat\n'

#def simulate(N, D, S, G, dt):
#        x0, v0, m = book.initial_cond(N, D)
#        for s in range(S):
#                with open(filename + str(s+1) +".dat", "w") as myfile:
#                        x1, v1 = book.timestep(x0, v0, G, m, dt)
#                        x0, v0 = x1, v1
#                        for n in range(N):
#				 myfile.write(str(x0[n,0]) + "  "
#					 + str(x0[n,1]) + "  " + str(x0[n,2]) + "\n")
#                        myfile.flush()
#    return '\nSimulation complete. Your data has been saved as ' + sys.argv[1] + '*.dat\n'


print simulate(int(N), int(D), int(S), float(G), float(dt))
