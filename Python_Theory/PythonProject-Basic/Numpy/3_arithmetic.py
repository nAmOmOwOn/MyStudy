import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr*arr)
print(arr-arr)
print(1/arr)
print(arr**0.5) # 자유롭게 연산이 됨

arr2 = np.array([[0,4,1],[7,2,12]])
print(arr2>arr) # True / False 로 반환 (조건식에 따라서)

