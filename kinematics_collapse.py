import numpy as np
import os


total_data = np.empty([0,77])

for fileName in os.listdir("/Users/clinic1718/Desktop/labeledData/"):
        if fileName[-4:] == ".txt":
                dataPath = "/Users/clinic1718/Desktop/labeledData/" + fileName
                data = np.loadtxt(dataPath)
                total_data = np.concatenate((total_data, data))

np.savetxt("kinematics.csv", total_data, delimiter=" ")