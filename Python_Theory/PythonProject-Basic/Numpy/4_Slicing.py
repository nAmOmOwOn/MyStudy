import numpy as np

arr = np.arange(10)
print(arr[5])
print(arr[5:8])
arr[5:8] = 12
print(arr)
print()

arr_slice = arr[5:8]
print(arr_slice)
arr_slice[1] = 12345
print(arr)
arr_slice[:] = 64 # 단순히 : 하면 배열의 모든 값을 할당함.
print(arr)
print()

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]]) # 다차원배열
print(arr2d)
print(arr2d[2])
print(arr2d[0][2]) # print(arr2d[0,2]) 이렇게 할 수도 있음.
print(arr2d[:2])
print(arr2d[:2,1:]) # 결과 보고 이해
print(arr2d[1,:2]) # 결과 보고 이해
print()

