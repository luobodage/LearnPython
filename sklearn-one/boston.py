# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 23:02:40 2020
波士顿房价数据集：load-boston（）：经典的用于回归任务的数据集
数据介绍：
该数据集是一个回归问题。每个类的观察值数量是均等的，共有 506 个观察，13 个输入变量和1个输出变量。
每条数据包含房屋以及房屋周围的详细信息。其中包含城镇犯罪率，一氧化氮浓度，住宅平均房间数，到中心区域的加权距离以及自住房平均房价等等。

@author: 王亚东
"""  

import numpy as np
import pandas as pd
from sklearn import datasets

#导入数据  协方差
boston = datasets.load_boston()
boston_X = boston.data
boston_X = pd.DataFrame(boston_X)
boston_y = boston.target
boston_corr = boston_X.corr()
# 数据规格化
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(boston_X)
X = scaler.transform(boston_X)
#主成分分析
from sklearn.decomposition import PCA
pca = PCA(0.85)
pca.fit(X)
Y = pca.transform(X)
#主成分参数
tzxl = pca.n_components_
tx = pca.explained_variance_
gxl = pca.explained_variance_ratio_
print (X)
print (Y)

G = 0
for i in np.arange(Y[0,:].size):
    G = G+ gxl[i]*Y[:,i]
