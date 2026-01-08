# Create a 3*3 narray that includes numbers from 1 to 9 and swap columns 1 and 2

import numpy as np
arr = np.arange(9).reshape(3,3)
print(arr)
arr[:,[1,2]] = arr[:,[2,1]]
print(arr)