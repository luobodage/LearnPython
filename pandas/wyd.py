import pandas as pd
import numpy as np
# #行列中最大的数值，哪个列包含每行的最大值 
# df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1))
# print(df)

# =============================================================================
# #滚动计算函数
# S=pd.Series(np.random.randint(1,100,20))
# print(S)
# print(S.rolling(10).mean())
# print(S.rolling(10).min())
# print(S.rolling(10).max())
# print(S.rolling(10).std())
# print(S.rolling(10).var())
# =============================================================================

# =============================================================================
# 
# dt = pd.DataFrame(np.random.randint(1,10,(5,6)))
# print(dt)
# print(dt.rolling(3).mean())
# 
# 
# df = pd.DataFrame(np.random.randint(1,10,(5,6)))
# print(df)
# s = df.apply(np.mean)
# print (s)
# 
# # groupby  分组
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#          'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#          'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#          'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#          'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# print(df)
# print (df.groupby('Year').groups)
# print (df.groupby(['Team','Year']).groups)
# 
# 
# #迭代遍历分组
# grouped = df.groupby('Year')
# for name,group in grouped:
#     print (name)
#     print (group)
#     
# #选择一个分组
# print (grouped.get_group(2014))
# 
# =============================================================================

#聚合函数为每个组返回单个聚合值。当创建了分组(group by)对象，就可以对分组数据执行多个聚合操作。 
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby('Year')
# print (grouped['Points'].agg(np.mean))

a = grouped.apply(lambda x: x.sort_values('Points', ascending=False))


print(df.sort_values('Points', ascending=False).groupby('Year').first().reset_index())#输出每年的点数第一

print(df.sort_values('Points', ascending=False).groupby('Year').head(2)) #输出每一年的点数前二 并且用点数排序

print(df.groupby('Team').head(2)) #输出每一年的点数前二 并且用点数排序






# print(grouped.apply(lambda x: x.sort_values('Rank', ascending=False)).groupby('Points').first().reset_index())

# print(c[c.score.rank(method = 'dense',ascending = False)==2]) 


# print (grouped.agg({'Points':np.mean,'Team':np.size}))


# print(a['mean'][2016])
