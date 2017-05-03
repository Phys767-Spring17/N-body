import numpy as np
import book as book


class cluster(object):
    """A cluster object is comprised of N unity masses
       starting at a random position in D-dimensional spce.
       
    """
    
    roar = "I am a cluster!\n"
    def __init__(self, partnum, clusnum, D, M):
        """initilizes the cluster object with the following parameters:
        
        param particle_cout: the number of particles in the simulation.
        param particle_dimensions: the number of dimensions.
        param cluster_count: the number of particle clusters.
        param cluster_dimensions: the number of dimensions
        param particle_positions: the x,y,z position of the particles
        param particle_velocities:
        param particle_masses:
        param cluster_position:
        """
        self.particle_count = partnum
        self.particle_dimensions = D
        self.cluster_count = clusnum
        self.cluster_dimensions = D
        self.particle_positions, self.particle_velocities, self.particle_masses = book.initial_cond(partnum, D)
        self.cluster_position = np.random.rand(1, D)*M
        
        
    def hear_me(self):
        """The hear me method is mostly for testing to ensure cluster properties exist for a cluster object.
        
        """
        myroar = self.roar + (
            "\n"
            "  My particle count is:          " + str(self.particle_count) + "\n" +
            "  My particle dimensions are:    " + str(self.particle_dimensions) + "\n" +
            "  My cluster count is:           " + str(self.cluster_count) + "\n" +
            "  My first particle position is: x: " + str(self.particle_positions[0,0]) + "\n" +
            "                                 y: " + str(self.particle_positions[0,1]) + "\n" +
            "                                 z: " + str(self.particle_positions[0,2]) + "\n" +
            "  My cluster count is:              " + str(self.cluster_count) + "\n" +
            "  My cluster position is:           " + str(self.cluster_position) + "\n")
        print(myroar)

    def cluster(self):
        """the cluster method returns the initial positions velocities and masses in the 
           same way the initial conditions function from the book module does. This allows
           for a seemless way to integrate the cluster object into existing simulations.
           
        """        
        x0 = self.particle_positions + self.cluster_position
        v0 = self.particle_velocities
        m = self.particle_masses
        return x0, v0, m
