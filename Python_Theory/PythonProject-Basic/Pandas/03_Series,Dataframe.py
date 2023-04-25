import pandas as pd
from pandas import Series, DataFrame
import numpy as np

pop = {'Nevada' : {2001: 2.4, 2002 : 2.9},
       'Ohio' : {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame3 = pd.DataFrame(pop)
print(frame3)
print()
print(frame3.T) # column 과 row 를 뒤집음
print(pd.DataFrame(pop, index=[2001,2002,2003]))
print()

pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada' : frame3['Nevada'][:2]}
print(pd.DataFrame(pdata))
print()

frame3.index.name = 'year'; frame3.columns.name = 'state'
print(frame3)
print()
print(frame3.values)