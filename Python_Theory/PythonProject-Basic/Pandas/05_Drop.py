import pandas as pd
import numpy as np

obj = pd.Series(np.arange(5.), index=['a','b','c','d','e'])
print(obj)

new_obj = obj.drop('c')
print(new_obj)
print(obj.drop(['d','c']))

data = pd.DataFrame(np.arange(16).reshape((4,4)), 
                    index=['Ohio','Colorado','Utah','New York'],
                    columns=['one','two','three','four'])
print(data)
print(data.drop(['Colorado','Ohio'])) # row 삭제
print(data.drop('two', axis=1)) # column 삭제
print(data.drop(['two','four'], axis='columns')) # column 삭제
obj.drop('c', inplace=True) # inplace 옵션을 사용하는 경우 버려지는 값이 모두 삭제됨! 주의
print(obj)