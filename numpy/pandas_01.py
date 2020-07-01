
# 提供了很多数据类型
# Series,DataFrame 基本操作、运算操作、特征类操作、关联类操作
import pandas as pd 
from pandas import Series,DataFrame
d = pd.Series(range(20))

dic = {'a':1,'b':2,'c':'as'}

dicSeries = Series(dic)
print(dicSeries)
print(dicSeries.index)

s = dicSeries.value_counts()

j = s.rolling(3).mean()
print(j)