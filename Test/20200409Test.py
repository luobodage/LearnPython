
import numpy as np 
import pandas as pd 
import time
# 第四题
# a = np.random.randint(0,100,(10,10))

# print(a)
# print(a.max())
# print(a.min())


# # 第五题
# nd  = np.zeros(shape = (10,10))
# nd[0:5,0:5] = 1
# nd[:-5,-5:] = 3
# nd[5:10,5:10] = 2
# nd[-5:,:-5] = 4
# print(nd)

# #第六题
# # f = ([np.arange(5)]*5)
# f=np.array([[0,1,2,3,4]]*5)
# print(f)

# #第七题
# nd=np.random.randint(1,10,10)
# nd[nd.argmax()]=0
# print(nd)

# # 第九题
# j=np.random.randint(0,100,size=(5,5))
# print(j)
# print()
# print(j[3].argsort())    #通过第二行返回一个索引
# print()
# print(j[j[3].argsort()]) #通过第二行返回一个索引 再排序输出

# #第十题
# nd=[1,2,3,4,5]

# nd1=np.vstack(nd)
# nd2=np.array([np.arange(8)]*5)
# nd3 = nd2[:,4:]
# nd4 = np.concatenate([nd1,nd3],axis=1)

# nd5 = nd4.reshape(1,25)
# nd6 = nd5[0][:21]
# print(type(nd5))
# print(nd5)
# print(nd6)

# a=np.random.randint(0,20,size=(3,4))
# print(a)
# print()
# print(a[:,[3,1,2,0]])

# a=np.random.rand(4,3)
# b=np.random.rand(3,4)
# o=np.dot(a,b)
# print(o)

# p=np.random.randint(0,5,(5,4))

# print(p-p.mean(axis=1).reshape(5,1))

# q=np.zeros(shape=(10,10))
# q1 = q+3
# q1[1::2,::2]=4
# q1[::2,1::2]=4
# print(q1)

# r=np.random.randint(0,10,(5,5))
# rmin=r.min()
# rmean = r.mean()
# rdown=r.max()-rmin
# rstd=r.std()
# print((r-rmean)/rstd)


a = np.random.randint(0,2,10)
b = np.random.randint(0,2,10)
c = a-b

print(a)
print(b)
print(c)
print("================================")
s = pd.value_counts(c)
print(s)
ss = s.sum() - s[0]
print(ss)