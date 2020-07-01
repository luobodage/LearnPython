# -*- coding: utf-8 -*-
import numpy as np
data1=np.load('data.npy')
data=data1[:,1:]
from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy='mean')
imp.fit(data)
data=imp.transform(data)

data =np.array([[0. , 0. , 0. ],
                [0.5, 0.5, 0.5],
                [1. , 2. , -4. ]])

from sklearn.preprocessing import StandardScaler
X=data
scaler = StandardScaler()
scaler.fit(X) 
X=scaler.transform(X)

print(np.mean(X,axis = 0),np.std(X,axis =0))




from sklearn.preprocessing import MinMaxScaler   
X1=data
min_max_scaler = MinMaxScaler()
min_max_scaler.fit(X1)
X1=min_max_scaler.transform(X1)

print(np.mean(X1,axis = 0),np.std(X1,axis =0))



from sklearn.preprocessing import minmax_scale  
X2=data
X2 = minmax_scale(X2,(1,100))


from sklearn.preprocessing import MaxAbsScaler
X3 = data
maxabscaler  = MaxAbsScaler()
x3 = maxabscaler.fit_transform(X3)


from sklearn.preprocessing import RobustScaler
X4 = data
a = RobustScaler()
X4 = a.fit_transform(X4)





