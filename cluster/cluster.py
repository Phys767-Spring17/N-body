import numpy as np
import book as book


class cluster(object):
    """A cluster is comprised of N unity masses
       starting at a random position in D-dimensional spce.
       
    """
    
    roar = "I am a cluster!\n"
    def __init__(self, partnum, clusnum, D, M):
        """
        """
        self.particle_count = partnum
        self.particle_dimensions = D
        self.cluster_count = clusnum
        self.cluster_dimensions = D
        self.particle_positions, self.particle_velocities, self.particle_masses = book.initial_cond(partnum, D)
        self.cluster_position = np.random.rand(clusnum, D)*M
        
        
    def hear_me(self):
        myroar = self.roar + (
            "\n"
            "  My particle count is:          " + str(self.particle_count) + "\n" +
            "  My particle dimensions are:    " + str(self.particle_dimensions) + "\n" +
            "  My cluster count is:           " + str(self.cluster_count) + "\n" +
            "  My first particle position is: x: " + str(self.particle_positions[0,0]) + "\n" +
            "                                 y: " + str(self.particle_positions[0,1]) + "\n" +
            "                                 z: " + str(self.particle_positions[0,2]))
 
        print(myroar)
