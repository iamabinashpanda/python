# For the numpy array given below perform the following operation:
# i.Convert the numpy array into a numpy matrix
# ii.Sort the values in a matrix

import numpy as np
arr = [[2,4,6],[1,3,5]]
arr = np.matrix(arr)
arr.sort(axis = 0)
print(arr)