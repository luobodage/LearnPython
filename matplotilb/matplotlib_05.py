import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False 

#随机x,y各十个散点图
plt.subplot(2,2,1)
x = np.random.rand(10)
y = np.random.rand(10)
plt.scatter(x, y)
#柱形图
plt.subplot(2,2,2)
x = np.arange(1, 6)
y = np.array([13, 15, 14, 17, 16])
plt.bar(x, y,color="green")
#饼状图
plt.subplot(2,2,3)
labels = ['1','2','3','4']
values = [10,30,45,15]
colors = ['red','green','blue','yellow']
plt.pie(values,labels=labels,colors=colors)
plt.show()