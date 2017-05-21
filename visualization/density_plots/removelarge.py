import numpy as np
import sys

filename = sys.argv[1]

data = np.loadtxt(filename)

x = data[:,0]
y = data[:,1]
z = data[:,2]

with open("proc_" + filename, "w") as myfile:
    for i in range(len(x)):
        if x[i] < 600 and x[i] > -100 and y[i] < 600 and y[i] > -100 and z[i] < 600 and z[i] > -100:
            myfile.write(str(x[i]) + " " + str(y[i]) + " "  + str(z[i]) + "\n")
    myfile.flush()
