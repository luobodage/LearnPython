# SeventhHomework.py

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False 

#作业：展示 各组车子中  运载人数 超过 700人的次数

data = pd.read_excel('一、车次上车人数统计表.xlsx')

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