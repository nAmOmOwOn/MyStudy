import pandas as pd
from pandas import Series, DataFrame
import numpy as np

data = {'state' : ['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],
        'year' : [2000, 2001, 2002, 2001, 2002, 2003],
        'pop' : [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

frame = pd.DataFrame(data)
print(frame)
print()
frame = pd.DataFrame(data, columns=['year','state','pop'])
print(frame)
print()
frame2 = pd.DataFrame(data, columns=['year','state','pop','debt'])
print(frame2) # column 에 하나 추가하면 값은 NaN 이 나옴
print()
print(frame2['state'])
print(frame2.year)
print(frame2.loc[2]) # 2인덱스 값을 가지는 row 출력!
frame2['debt'] = np.arange(6.) # column 들의 값을 넣을 수 있음
print(frame2)