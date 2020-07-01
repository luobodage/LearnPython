# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 22:49:17 2020

鸢尾花数据集：load_iris（）：用于分类任务的数据集
数据介绍：
一般用于做分类测试
有150个数据集，共分为3类，每类50个样本。每个样本有4个特征。
每条记录都有 4 项特征：包含4个特征（Sepal.Length（花萼长度）、Sepal.Width（花萼宽度）、Petal.Length（花瓣长度）、Petal.Width（花瓣宽度）），特征值都为正浮点数，单位为厘米。
可以通过这4个特征预测鸢尾花卉属于（iris-setosa（山鸢尾）, iris-versicolour（杂色鸢尾）, iris-virginica（维吉尼亚鸢尾））中的哪一品种。

@author: 王亚东
"""

import numpy as np
import pandas as pd
from sklearn import datasets

#导入数据  协方差
iris = datasets.load_iris()
iris_X = iris.data
iris_X = pd.DataFrame(iris_X)
iris_y = iris.target
iris_corr = iris_X.corr()
# 数据规格化
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(iris_X)
X = scaler.transform(iris_X)
#主成分分析
from sklearn.decomposition import PCA
pca = PCA(0.98)
pca.fit(X)
Y = pca.transform(X)
#主成分参数
tzxl = pca.n_components_
tx = pca.explained_variance_
gxl = pca.explained_variance_ratio_
print (X)
print (Y)

F = gxl[0]*Y[:,0]+gxl[1]*Y[:,1]+gxl[2]*Y[:,2]

G = 0
for i in np.arange(Y[0,:].size):
    G = G+ gxl[i]*Y[:,i]