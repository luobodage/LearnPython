import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False 

#x**2 + y**2 = 1 圆
x1 = np.arange(-1,1,0.00001)
y1 = np.sqrt(1-x1*x1) # y1 = (1 - x1*x1)开根号
x2 = np.arange(-1,1,0.00001)
y2 = -1*np.sqrt(1-x2*x2)

plt.plot(x1,y1,x2,y2,color="red")
plt.title("圆")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
