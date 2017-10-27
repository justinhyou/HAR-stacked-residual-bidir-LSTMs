"""
create X_test.txt and y_test.txt for JIGSAW kinematics


make changes to this code to correctly point to the labeled data directory for the kinematics data
(or process from product of kinematics_collapse)

"""

import numpy as np
import os

features = np.empty([0, 76])
labels = np.empty([0,1])

for fileName in os.listdir("/Users/clinic1718/Desktop/labeledData/"):
        if fileName[-4:] == ".txt":
                dataPath = "/Users/clinic1718/Desktop/labeledData/" + fileName
                data = np.loadtxt(dataPath)
                features = np.concatenate((features,data[:,:-1]))
                labels = np.concatenate((labels,data[:,-1]))

np.savetxt("kinematics.txt", labels, delimiter=" ")
np.savetxt("kinematics.txt", features, delimiter=" ")