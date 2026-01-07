# In the numpy array given below print all the elements ranging from 8 to 15.

import numpy as np
arr = [1,2,3,4,5,8,9,10,12,22,32,54,99,6,7]
arr = np.array(arr)
print(arr[(arr>=8)&(arr<=15)])
