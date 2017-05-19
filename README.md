The functions used in this code were taken from Effective_Computation_in_Physics chapter 12. 

This code is a numerical simulation based on Newtons laws of gravity. Three versions of the
numerical simulation were created. 

# _**Program Versions:**_

## _**The first version**_ 
Is found in the simulation directory is named gravsim.py. The program defines and
calls a function named simulate. The simulate function from the book was modified to save the 
calculated particle positions to a file for each time step taken. The remaining functions taken
from the book are stored in the book directory in a file named book.py. gravsim.py calls
book.py as a module and generates a single cluster of N unit mass particles randomly placed 
using np.random.

## _**The second version**_
Is found in the parallel directory was also taken from the book. This code was
modified in the same way as the first version to save output. The program is different from the first
version in that it creates a user defined number of threads to perform calculations in parallel. 
As the book describes the benefit of this form of parallelization decays quickly as the number
of threads increases.

## _**The third version**_
Is found in the cluster directory uses the first version of the code along with
a class named cluster. The cluster class allows the user to generate multiple randomly placed
clusters of particles each defined in the same manner as the single cluster defined in first version.
The main purpose for creating this version was to produce a visually interesting set of data
to be using for the visualization section.

## _**Visualization**_
Was done using basic python plotting and animation as well as density plots found on
stackoverflow.com. While the simulations are able to perform calculations for an arbitrary number
of particle dimensions; the plotting programs are currently configured for three dimensional
input and two dimensional output. Sample data can be found in the visualization directory.

## _**Installation and Execution**_ 
Run setup.sh to export the book directory to PYTHONPATH. Then you will
be able to run any of the versions of the codes from their respective directories. The first and
second simulations will perform calculations based on user input. When running the first and second
version exceptions will be reasied and instructions of use provided when the program is not used
correctly. An example run could be the following.

    python gravsim.py out_file_name 100 3 100 1 1e-3

The arguments following the out_file_name are particle number, dimensions, number of time steps,
gravitational constant, and time step. This example would generate 100 files with the name
out_file_name*.data, where the * is a number from 1 to 100. Each file will contain the x, y, and z
coordinates of the 100 particles. An animation can then be generated using animation.py, found in 
the visualization/plots/ directory. Any individual file can also be plotted using scatter_plot.py,
also found in the visualization/plots directory. And finally any individual plot can be plotted
using density_plot.py, found in the visualization/density_plots directory.

N-body  
├── book  
├── cluster  
├── parallel  
│   └── threads  
├── simulation  
├── tests  
└── visualization  
&nbsp;&nbsp;&nbsp;├── density_plots  
&nbsp;&nbsp;&nbsp;├── output_examples  
&nbsp;&nbsp;&nbsp;└── plots  
