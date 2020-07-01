import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False 

#作业：展示 各组车子中  运载人数 超过 700人的次数

data = pd.read_excel('C:/Users/萝卜ovo/Desktop/Python/一、车次上车人数统计表.xlsx')

#筛选700以上并返回多少次函数
def bigseven(i):
	tb = data[data['车次'] == 'D0' + str(i)].sort_values('日期')
	p = []
	for x in range(len(tb.iloc[:,[0]])-1):
		s = tb.iloc[x,2]
		if (int(s)>700):
			p.append(s)
	return len(p)


w = []
for y in [2,3,4,5,6]:
	w1 = bigseven(y)
	w.append(w1)

print((w))
c = ['D02','D03','D04','D05','D06']

plt.pie(w,labels=c)
plt.show()


#求和函数
# def sumtb(i):
# 	tb = data[data['车次']=='D0'+str(i)].sort_values('日期')
# 	l = tb.iloc[0,2:].sum()
# 	return l

# l = []
#
# for x in [2,3,4,5,6]:
# 	l1 = sumtb(x)
# 	l.append(l1)
#
# print(l)
#

#
# # p1 = (l1+l2)/l1
# # p2 = (l1+l2)/l2
#
# # q = [p1,p2]
# # x = np.arange(0,24,1)
#
# # y = tb.iloc[:,2]
#
# # plt.figure(figsize = (8,8))
#
# # plt.xlabel('日期')
# # plt.ylabel('人数')
# # plt.xticks([1,5,10,15,20],tb['日期'].values[[0,4,9,14,19]],rotation=45)
# # plt.scatter(x,y)    #离散点
# # plt.bar(c,d)
# plt.pie(l,labels=c)
# plt.show()