import numpy as np

x = np.array([[1,2,3],[4,5,6]])

y = np.array([[6,23],[-1,7],[8,9]])

print(x.dot(y)) # 행렬의 곱셈 np.dot(x,y) 와 동일
print(np.dot(x, np.ones(3))) # ones = 1로 가득찬 행렬 ones(3) = (1,1,1)세로로
print(x @ np.ones(3)) # 위 코드와 같음
