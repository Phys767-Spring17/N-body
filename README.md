The functions used in this code were taken from Effective_Computation_in_Physics chapter 12. 

This code is a numerical simulation based on Newtons laws of gravity. Three versions of the
numerical simulation were created. 

The first version, found in the simulation directory is named gravsim.py. The program defines and
calls a function called simulate. The simulate function was taken from the book and modified to
save the calculated particle positions to a file for each time step taken. gravsim.py calls the
book.py module (found in the book directory and contains all the functions defined in the book) and
generates a single cluster of N unit mass particles randomly placed useing np.random.

The second version, found in the parallel directory was also taken from the book. This code was
modified in the same way as the first version to save output. The program is different from the first
version in that it creates a user defined number of threads to perform calculations in parallel. 
As the book describes the benefit of this form of parallelization decays quickly as the number
of threads increases.

The third version, found in the cluster directory uses the first version of the code along with
a class named cluster. The cluster class allows the user to generate multiple randomly placed
clusters of particles each defined in the same manner as the single cluster defined in first version.

Visualization was done using basic python plotting and animation methods and the creation of density
plots. The code for the density plots was found on stackoverflow.com. 

