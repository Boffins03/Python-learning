import numpy as np
arr = np.array([2,5,6,73,2])

x = arr.copy()
y = arr.view()

x[0] = 54
y[0] = 84

print(arr , x, y)
print(x.base, y.base)