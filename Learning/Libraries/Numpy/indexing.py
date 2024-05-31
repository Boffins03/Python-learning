import numpy as np

arr1 = np.array([2,5,6,4,2])
arr2 = np.array([[2,5,7,3,7,9],[4,6,7,8,2,2]])
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# indexing 
print(arr1[4])  # print(2)
print(arr2[0,5]) # print(9)
print(arr3[1,1,2]) # print(12)

# slicing
arr = np.array([10, 15, 20, 25, 30, 35, 40])

print(arr[1:4])

