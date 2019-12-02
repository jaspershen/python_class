import numpy as np
import pandas as pd
from dfply import *

obj = pd.Series([4, 7, -5, 3])

obj.values
obj.index
obj.index << list


obj.index << len


list(obj.index)


obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

obj2


len(obj2)

import dfply

obj2 >> len()


obj2[['c', 'a', 'd']]


sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

states = ['California', 'Ohio', 'Oregon', 'Texas']

obj4 = pd.Series(sdata, index=states)

pd.isnull(obj4)

pd.isna(obj4)

pd.notna(obj4)

obj4.isna()

obj4.isnull


obj4.name

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002, 2003],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

frame

frame.head()

pd.DataFrame(data, columns=['year', 'state', 'pop'])

frame
type(frame)


frame.columns

frame.index


frame['state']

frame.state

frame.iloc[1]

frame.iloc[1:3]

del frame2['eastern']

frame3 = pd.DataFrame(pop)

frame3


frame

frame.T

obj = pd.Series(range(3), index=['a', 'b', 'c'])

obj
index = obj.index

index

type(index)


list(index)

tuple(index)

dict(index)



np.array(index)

index


pd.Series(index)

pd.DataFrame(index)

frame

frame.reindex()

obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])

obj3

obj3

obj3[0:3]


obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])


obj[2:4]


obj3

type(obj3)


ser = pd.Series(np.arange(3.))

ser

ser[0]


df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))

df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))

df1

df2

df2.loc[1]

df2.loc[1,:]


frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])


frame


frame.apply(lambda x: np.mean(x), axis=1)

frame.apply(lambda x: np.mean(x), axis=0)


frame.apply(lambda x: (x - np.mean(x))/np.std(x), axis=1)

frame.sort_index()

frame.sort_index(axis = 1)

frame.sort_index(ascending=False)

frame.sort_values()