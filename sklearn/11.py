from sklearn.datasets import load_boston
boston = load_boston()
 
from sklearn.cross_validation import train_test_split
import numpy as np
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=33,test_size=0.25)
#分析一下数值的差异
print('最大值',np.max(boston.target))
print('最大值',np.min(boston.target))
print('均值',np.mean(boston.target))
 
#对数据进行预处理 预处理模块 StandardScaler fit() 模型训练 transform fit_transform
#标准化处理
from sklearn.preprocessing import *
 
ss_x=StandardScaler()
ss_y=StandardScaler()
 
#分别对训练集合测试集 及特征值进行标准化处理
#
x_train=ss_x.fit_transform(x_train)
x_test = ss_x.transform(x_test)
 
#将标签数据转换为 m行1列
y_train = np.array(y_train).reshape(-1,1)
y_train = ss_y.fit_transform(y_train)
y_test = np.array(y_test).reshape(-1,1)
y_test = ss_y.transform(y_test)
rom sklearn.linear_model import LinearRegression
 
lr = LinearRegression()
lr.fit(x_train,y_train)
lr_predict_value = lr.predict(x_test)
print(y_test[:10])
print(lr_predict_value[:10])
print('各列权重',lr.coef_)
print('训练集上的评分',lr.score(x_train,y_train))
print('测试集上的评分',lr.score(x_test,y_test))·