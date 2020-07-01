# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 23:42:19 2020
datasets.fetch_olivetti_faces()
@author: 王亚东
"""
from scipy.io import loadmat
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression,Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import ExtraTreesRegressor
import sklearn.datasets as datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


#导入数据  协方差
fetch_olivetti_faces = loadmat("olivettifaces.mat")
fetch_olivetti_faces_X = fetch_olivetti_faces['faces']
fetch_olivetti_faces_X = fetch_olivetti_faces_X.T
fetch_olivetti_faces_X = pd.DataFrame(fetch_olivetti_faces_X)
#fetch_olivetti_faces_corr = fetch_olivetti_faces_X.corr()



data1 = fetch_olivetti_faces_X               # (400, 4096)

data = data1.values


# 对data数据进行拆分，拆分成上半部分脸（训练样本集）和下半部分脸（目标值）
face_up = data[:, :2048]        # (400, 2048)
face_down = data[:, 2048:]
X_train,X_test,y_train,y_test = train_test_split(face_up, face_down, test_size = 0.02)

# 创建机器学习模型，以字典的形式包含四种模型
estimators = {"linear":LinearRegression(),
             "ridge":Ridge(alpha = 0),
             "knn":KNeighborsRegressor(),
             "extratree":ExtraTreesRegressor()}
            
face_pred = dict()          # 定义一个字典保存预测结果
for key,estimator in estimators.items():
    estimator.fit(X_train,y_train)
    y_ = estimator.predict(X_test)
    face_pred[key] = y_      

# 绘图（8行6列）
plt.figure(figsize=(18,24))
for i in range(8):
	# 第一列的数据，放真实的人脸
    axes = plt.subplot(8,6, i*6+1)
    face_up = X_test[i]
    face_down = y_test[i]
    face = np.concatenate([face_up,face_down])
    axes.imshow(face.reshape((64,64)),cmap = "gray")
    # 第二列的数据， 放真实的上半部分脸
    axes2 = plt.subplot(8,6,i*6+2)
    face_up = X_test[i]
    axes2.imshow(face_up.reshape(32,64), cmap = "gray")   
    # 三至六列放回归之后的数据
    for j, key in enumerate(face_pred):
        '''(0, 'linear')
            (1, 'ridge')
            (2, 'knn')
            (3, 'extratree')'''
        axes = plt.subplot(8,6,i*6+3+j)
        if i == 0:
            axes.set_title(key)
        face_up = X_test[i]
        y_ = face_pred[key]
        # 预测的下半部分脸的目标值
        face_down_pred = y_[i]
        face = np.concatenate([face_up, face_down_pred])
        axes.imshow(face.reshape(64,64), cmap = "gray")  
