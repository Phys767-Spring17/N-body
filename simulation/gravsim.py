# -*- coding: utf-8 -*-
#!/usr/bin/python   ##Shabang!

########################################################################################################
#                                                                                                      #
#    Written by:                                                                                       #
#                                                                                                      #
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
#very obnoxious mode: Active                                                                           #
########################################################################################################


import book  # functions taken from book packaged as a module.
import sys
import os  # modules used to fancify user interface.


def input_check(n):
    """run time argument handling of user defined values.
    A total of 7 arguments must be included at run time
    as defined by the error message listed below.

    :param n: number of command line arguments
    :return: params for simulations.
    """
    if len(sys.argv) == n:
     filename = sys.argv[1]
     N = sys.argv[2]
     D = sys.argv[3]
     S = sys.argv[4]
     G = sys.argv[5]
     dt = sys.argv[6]
     return filename, N, D, S, G, dt


def input_int_check(N, D, S):
    """conditional check for integer values of N, D, and S.

    :param N: The number of particles in the simulation.
    :param D: The number of dimensions.
    :param S: The number of time steps to be used for the simulation.
    :return: N/A
    """
    N.isdigit()
    D.isdigit()
    S.isdigit()


def usage_error():
    """Prints to screen how to use the program when the user raises an error.
    
    """
    print('\n    The proper use of gravsim.py is as follows.')
    print('\n        python gravsim.py outputfile N D S G dt\n')
    print('    Simulate function from Computation book modified to take in\n'
           "    user specified variables N, D, S, G, dt and output a user specified\n"
           "    file name.\n"

           "    :param N: The number of particles.\n"
           "    :param D: The number of dimensions.\n"
           "    :param S: The number of time steps.\n"
           "    :param G: Gravitational constant.\n"
           "    :param dt: The time step.\n")


def simulate(N, D, S, G, dt):
    """Simulate function from Computation book modified to take in
    user specified variables N, D, S, G, dt and output a user specified
    file name.

    :param N: The number of particles.
    :param D: The number of dimensions.
    :param S: The number of time steps.
    :param G: Gravitational constant.
    :param dt: The time step.
    :return: Simulation complete message.
    """
    x0, v0, m = book.initial_cond(N, D)
    for s in range(S):
        with open(filename + str(s+1) + ".dat", "w") as myfile:
            x1, v1 = book.timestep(x0, v0, G, m, dt)
            x0, v0 = x1, v1
            for n in range(N):
                myfile.write(str(x0[n, 0]) + "  " + str(x0[n, 1]) + "  " + str(x0[n, 2]) + "\n")
            myfile.flush()
    return '\nSimulation complete. Your data has been saved as ' + sys.argv[1] + '*.dat\n'


while True:
    try:
        filename, N, D, S, G, dt = input_check(7)
        input_int_check(N, D, S)
        print(simulate(int(N), int(D), int(S), float(G), float(dt)))
        break
        except (TypeError, NameError):
            print('\n    TypeError:  You did not provide enough input values.\n')
            usage_error()
            break
        except ValueError:
            usage_error()
            break
