import pandas as pd
import numpy as np

obj3 = pd.Series(['blue','purple','yellow'], index=[0,2,4])
print(obj3)
print(obj3.reindex(range(6), method='ffill')) # 누락된 인덱스에 그 전 값들을 전이나 후 값을 채워 넣음
print()

frame = pd.DataFrame(np.arange(9).reshape((3,3)), index=['a','c','d'], columns=['Ohio','Texas','California'])
print(frame)
frame2 = frame.reindex(['a','b','c','d'])
print(frame2)
states = ['Texas','Utah','California']
print(frame.reindex(columns=states))