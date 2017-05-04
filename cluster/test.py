import cluster as cl
import book


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
    x = cl.cluster(3, 2, 3, 1000) #partnum clustnum D M: create cluster object

    x0, v0, m = x.cluster()   
#   x0, v0, m = book.initial_cond(N, D)
    for s in range(S):
        with open("clusterdata" + str(s+1) +".dat", "w") as myfile:
            x1, v1 = book.timestep(x0, v0, G, m, dt)
            x0, v0 = x1, v1
            for n in range(N):
                myfile.write(str(x0[n,0]) + "  " + str(x0[n,1]) + "  " + str(x0[n,2]) + "\n")
            myfile.flush()
    return '\nSimulation complete. Your data has been saved as clusterdata*.dat\n'



print(simulate(3, 3, 1, 1, 1e-3))


#x = cl.cluster(3, 2, 3, 1000) #partnum clustnum D M
#x.hear_me()
#print
#for i in range(x.particle_count):
#	print x.particle_positions[i,0], x.particle_positions[i,1], x.particle_positions[i,2]
#print
#print x.particle_positions



