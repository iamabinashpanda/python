# In the given numpy array replace the NaN values with the average of columns

import numpy as np
arr= np.array([[1.3, 2.5, 3.6, np.nan], [2.6, 3.3, np.nan, 5.5], [2.1, 3.2, 5.4, 6.5]])
print(arr)
col_mean = np.nanmean(arr,axis=0)
ind = np.where(np.isnan(arr))
arr[ind] = np.take(col_mean,ind[1])
print(arr)