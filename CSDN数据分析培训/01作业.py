import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import jqdatasdk as jq


#登录jqdata
jq.auth('18846936702','Zxc4525577')

#获取数据
data = jq.get_price("601766.XSHG",start_date="2020-07-01",end_date="2020-08-08",fields=['open','close','high','low'])

df = pd.DataFrame(data)

dfs = (df['high']-df['low'])/df['low']
dfup = df['close']/df['open']-1
y1 = dfup
x = dfs.index
y = dfs

fig = plt.figure(figsize=(16,6))
left,bottom,width,height = 0.1,0.1,0.8,0.8
ax1 = fig.add_axes([left,bottom,width,height])
ax1.plot(x,y,'blue')

x1 = np.array([1,2,3,4,5])

left,bottom,width,height = 0.64,0.5,0.2,0.3
ax2 = fig.add_axes([left,bottom,width,height])
ax2.plot(x1,x1*x1,'red',x1,x1*2,'green')



plt.show()



