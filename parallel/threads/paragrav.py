#!/usr/bin/python  ##Shabang!

# import matplotlib  # These two lines are only needed
# matplotlib.use('Agg')  # if you are running this via ssh

import paraBook as book  # functions taken from book packaged as a module.
import sys  # modules used to fancify user interface.


def input_check(n):
    """run time argument handling of user defined values.
    A total of 7 arguments must be included at run time
    as defined by the error message listed below.

    :param n: number of command line arguments
    :return: params for simulations.
    """
    if len(sys.argv) == n:
     filename = sys.argv[1]
     P = sys.argv[2]
     N = sys.argv[3]
     D = sys.argv[4]
     S = sys.argv[5]
     G = sys.argv[6]
     dt = sys.argv[7]
     return filename, P, N, D, S, G, dt


def input_int_check(P, N, D, S):
    """conditional check for integer values of N, D, and S.

    :param P: The number of threads.
    :param N: The number of particles in the simulation.
    :param D: The number of dimensions.
    :param S: The number of time steps to be used for the simulation.
    :return: N/A
    """
    P.isdigit()
    N.isdigit()
    D.isdigit()
    S.isdigit()


def usage_error():
    """Prints to screen how to use the program when the user raises an error.
    
    """
    print('\n    The proper use of gravsim.py is as follows.')
    print('\n        python gravsim.py outputfile N D S G dt\n')
    print('    Simulate function from Computation book modified to take in\n'
           "    user specified variables P, N, D, S, G, dt and output a user specified\n"
           "    file name.\n"

           "    :param P: The number of threads.\n"
           "    :param N: The number of particles.\n"
           "    :param D: The number of dimensions.\n"
           "    :param S: The number of time steps.\n"
           "    :param G: Gravitational constant.\n"
           "    :param dt: The time step.\n")


#def input_check(n):
#    """run time argument handling of user defined values.
#    A total of 7 arguments must be included at run time
#    as defined by the error message listed below.

#    :param n: number of command line arguments
#    :return: params for simulations.
#    """
#    if len(sys.argv) == n:
#        filename = sys.argv[1]
#        P = sys.argv[2]
#        N = sys.argv[2]
#        D = sys.argv[3]
#        S = sys.argv[4]
#        G = sys.argv[5]
#        dt = sys.argv[6]
#        return filename, N, D, S, G, dt
#    else:
#        print('\n    The proper use of gravsim.py is as follows.')
#        print('\n        python gravsim.py outputfile N D S G dt\n')
#        print('    Simulate function from Computation book modified to take in\n'
#               "    user specified variables N, D, S, G, dt and output a user specified\n"
#                "    file name.\n"

#                "    :param N: The number of particles.\n"
#                "    :param D: The number of dimensions.\n"
#                "    :param S: The number of time steps.\n"
#                "    :param G: Gravitational constant.\n"
#                "    :param dt: The time step.\n")
#        os._exit(1)
    

#def input_int_check(N, D, S):
#    """conditional check for integer values of N, D, and S.
    
#    :param N: The number of particles in the simulation.
#    :param D: The number of dimensions.
#    :param S: The number of time steps to be used for the simulation.
#    :return: N/A
#    """
#    for i in range(6):
#        i = 2
#        test = sys.argv[i]
#        if test.isdigit():
#            continue
#        else:
#            print('\nN, D, and S must be integers\n')
#            os._exit(1)
          

def simulate(P, N, D, S, G, dt):
    """Simulate function from Computation book modified to take in
    user specified variables P, N, D, S, G, dt and output a user specified
    file name.
    
    :param P: The number of threads
    :param N: The number of particles.
    :param D: The number of dimensions.
    :param S: The number of time steps.
    :param G: Gravitational constant.
    :param dt: The time step.
    :return: Simulation complete message.
    """
    x0, v0, m = book.initial_cond(N, D)
    pool = book.Pool(P)
    for s in range(S):
        with open(filename + str(s+1) + ".dat", "w") as myfile:
            x1, v1 = book.timestep(x0, v0, G, m, dt, pool)
            x0, v0 = x1, v1
            for n in range(N):
                myfile.write(str(x0[n, 0]) + "  " + str(x0[n,1]) + "  " + str(x0[n, 2]) + "\n")
            myfile.flush()
    return '\nSimulation complete. Your data has been saved as ' + sys.argv[1] + '*.dat\n'



#filename, P, N, D, S, G, dt = input_check(8)
#input_int_check(N, D, S)

#print(simulate(int(P) ,int(N), int(D), int(S), float(G), float(dt)))  # get the party started!


while True:
    try:
        filename, P, N, D, S, G, dt = input_check(8)
        input_int_check(P, N, D, S)
        print(simulate(int(P), int(N), int(D), int(S), float(G), float(dt)))
        break
    except(TypeError, NameError):
        print('\n    TypeError:  You did not provide enough input values.\n')
        usage_error()
        break
    except ValueError:
        print('\n    ValueError: P, N, D, and S must be integers\n')
        usage_error()
        break
