import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False 

x = np.arange(0,10,0.2)
print(x)

y = np.sin(x)
plt.title('sin曲线')
plt.plot(x,y,color="red")
plt.show()

y = np.cos(x)
plt.title('cos曲线')
plt.plot(x,y)
plt.show()
plt.savefig('quxian',dpi=600)