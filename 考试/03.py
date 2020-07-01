import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error #平方绝对误差


boston = datasets.load_boston()
print(boston.DESCR)       #获得关于房价的描述信息
x = boston.data       #获得数据集的特征属性列
y = boston.target       #获得数据集的label列
df = pd.DataFrame(data = np.c_[x,y],columns=np.append(boston.feature_names,['MEDV'])) #np.c_是按列连接两个矩阵，就是把两矩阵左右相加，要求列数相等
df = df[['RM','MEDV']]      #选择房间数属性列和房价属性列
print(df[:5])         #查看前5行的数据格式

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.4)     #划分数据集

scaler = StandardScaler()        #作用：去均值和方差归一化。可保存训练集中的均值、方差参数，然后直接用于转换测试集数据。
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

linreg = LinearRegression()
model = linreg.fit(x_train,y_train)

print("MSE均方误差：",mean_squared_error(y_train,model.predict(x_train)))
print("RMSE均方根误差：",mean_squared_error(y_train,model.predict(x_train)) ** 0.5)
print("MAE平均绝对误差：",mean_absolute_error(y_train,model.predict(x_train)))
print("r2_score决定系数：",r2_score(y_train,model.predict(x_train)))
