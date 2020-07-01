# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:52:22 2020

@author: 萝卜ovo
"""

import matplotlib.pyplot as plt 

plt.plot([0,2,4,6,8][3,1,4,5,2])
plt.ylabel("grade")
plt.axis([-1,10,0,6]) #x轴以-1开始10结束 y轴以0开始6结束
plt.savefig('折线图',dpi=600) #保存一个png格式的图片 dpi输出质量
plt.show()