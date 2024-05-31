import numpy as np

arr = np.array(((1,4,56,6,2,3,4),(3,5,6,2,4,122,3)))

print(arr)
print(arr.shape)

print(arr.reshape(-1)) # Flattening the array

arr = np.array((3,5,6,0,8,3,2,11,3))
print(arr.reshape(3,3))