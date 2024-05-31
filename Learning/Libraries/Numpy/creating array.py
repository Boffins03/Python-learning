import numpy as np
# 0-D array
arr = np.array(42)
print(arr)
print(arr.ndim)

# 1-D array
arr = np.array([42,32])
print(arr)
print(arr.ndim)

# 2-D array
arr = np.array([[42,42],[4,6]])
print(arr)
print(arr.ndim)

# 3-D array
arr = np.array([[[42,53],[23,53]], [[23,56],[34,64]]])
print(arr)
print(arr.ndim)

# higher D array
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

# datatype check
print(arr.dtype)