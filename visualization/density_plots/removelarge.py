import numpy as np

x, y, z = np.loadtxt("temp1000.data", delimiter=' ', unpack=True)

with open("proctemp1000.data", "w") as myfile:
    for i in range(len(x)):
        if x[i] < 600 and x[i] > -100 and y[i] < 600 and y[i] > -100 and z[i] < 600 and z[i] > -100:
            myfile.write(str(x[i]) + " " + str(y[i]) + " "  + str(z[i]) + "\n")
    myfile.flush()
