import pandas as pd
from pandas import Series, DataFrame

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