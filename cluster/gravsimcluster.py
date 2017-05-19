import numpy as np
import cluster as cl
import book


def simulate(N, M, D, S, G, dt):
    """Simulate function from Computation book modified to take in
    user specified variables N, D, S, G, dt and output a user specified
    file name.

    :param N: The number of particles.
    :param M: The number of clusters.
    :param D: The number of dimensions.
    :param S: The number of time steps.
    :param G: Gravitational constant.
    :param dt: The time step.
    :return: Simulation complete message.
    """
    x = cl.cluster(N, M, D, 500)  # create cluster object. 500 defines the maximum position coordinate of a cluster.
    x0, v0, m = x.cluster()  # x0, v0, m = book.initial_cond(N, D) <-- old way to initialize
    for s in range(S):
        with open("clusterdata" + str(s+1) + ".dat", "w") as myfile:
            for i in range(M):
                x1, v1 = book.timestep(x0[i], v0[i], G, m[i], dt)
                x0[i], v0[i] = x1, v1
                myfile.write(str(x0[i]).replace('[', '').replace(']', '') + "\n")
            myfile.flush()
    return '\nSimulation complete. Your data has been saved as clusterdata*.dat\n'


np.set_printoptions(threshold='nan')  # This is needed to print the entire x0 array to file.

N = 1000
M = 100
D = 3
S = 1000
G = 1
dt = 1e-3

print(simulate(N, M, D, S, G, dt))  # Run the simulation!
