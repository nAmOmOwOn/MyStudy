import numpy as np

arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9,],[10,11,12]]])
print(arr3d)
print(arr3d[0])
old_values = arr3d[0].copy()
arr3d[0] = 42
print(arr3d)
print(arr3d[1,0])
x = arr3d[1]
print(x)
print(x[0])