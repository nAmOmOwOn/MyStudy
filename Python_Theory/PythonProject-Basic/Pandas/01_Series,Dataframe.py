import pandas as pd
from pandas import Series, DataFrame

sdata = {'Ohio' : 35000,
         'Texas' : 71000,
         'Oregon' : 16000,
         'Utha' : 5000
         }

obj3 = pd.Series(sdata)
print(obj3)
print()

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)
print(pd.isnull(obj4)) # = obj4.isnull()
print(pd.notnull(obj4))
print()

print(obj3 + obj4)
print()