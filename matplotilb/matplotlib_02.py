import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei'

def f(t):
	return np.exp(-t) * np.cos(2*np.pi*t)

a = np.arange(0.0,5.0,0.02)

plt.subplot(211)
plt.plot(a,f(a))

plt.subplot(2,1,2)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.show()


a = np.arange(10)

plt.plot(a)
plt.ylabel("纵轴")
plt.show()