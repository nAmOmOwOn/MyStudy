import numpy as np

arr = np.random.randn(100)
print((arr > 0).sum()) # 양수인 원소의 개수

bools = np.array([False, False, True, False])
print(bools.any()) # 하나 이상의 값이 True 이면 True 반환 아니면 False
print(bools.all()) # 모든 값이 True 이면 True 반환 아니면 False