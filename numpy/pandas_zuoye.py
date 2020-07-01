import pandas as pd 
import numpy as np 

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby('Year')

print("-----输出每年的点数第一名-----")

print(df.sort_values('Points', ascending=False).groupby('Year').first())#输出每年的点数第一名

print("----输出每一年的点数前二 并且用点数排序----")

print(df.sort_values('Points', ascending=False).groupby('Year').head(2)) #输出每一年的点数前二 并且用点数排序

print("-----每一年的点数第二名-----")
# 输出每一年的点数第二名
for x,y in grouped:
    # print (x)
    print (y.sort_values('Points',ascending=False).groupby('Year').head(2)[1:2])

