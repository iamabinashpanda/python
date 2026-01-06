# Convert the given list in to a numpy array and replace the odd elements with -2

import numpy as np
Lst=[[1,2,3], [4,5,6], [7,8,9]]
arr = np.array(Lst)
arr[arr%2!=0] = -2
print(arr)