import numpy as np

arr = np.random.randn(4,4) # 4 x 4 행렬 배열 생성
print(arr.shape) # 행 열 보여주는 식
print(arr.dtype) # 데이터 타입

print(arr)
print(np.where(arr > 0, 2, -2)) # arr 성분의 크기가 0보다 크면 2, 아니면 -2로

data1 = [6,7.5,8,0,1]
arr1 = np.array(data1) # numpy 배열 생성
print(arr1)

data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2) # numpy 다차원 배열 생성
print(arr2)
print(arr.ndim) # 배열의 차원 수 or 배열의 축 수

print(np.arange(10)) # arange = python range 와 비슷함