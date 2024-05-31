import numpy as np

arr = np.array([2,4,6,7],dtype="S")

print(arr)
print(arr.dtype)

newarr = arr.astype('b')
print(newarr)
