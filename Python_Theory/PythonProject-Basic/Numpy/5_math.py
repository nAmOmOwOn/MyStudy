import numpy as np

arr = np.random.randn(5,4)
print(arr)
print(arr.mean()) # 평균
print(np.mean(arr)) # 평균
print(arr.sum()) # 합계
print(arr.mean(axis = 1)) # column 의 평균
print(arr.sum(axis = 0)) # row 의 합
print()

arr = np.array([0,1,2,3,4,5,6,7])
print(arr.cumsum()) # 누적 합