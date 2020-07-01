# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 23:38:41 2020
datasets.load_breast_cancer()
@author: 王亚东
"""


import numpy as np
import pandas as pd
from sklearn import datasets

#导入数据  协方差
breast_cancer = datasets.load_breast_cancer()
breast_cancer_X = breast_cancer.data
breast_cancer_X = pd.DataFrame(breast_cancer_X)
breast_cancer_y = breast_cancer.target
breast_cancer_corr = breast_cancer_X.corr()
# 数据规格化
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(breast_cancer_X)
X = scaler.transform(breast_cancer_X)
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

G = 0
for i in np.arange(Y[0,:].size):
    G = G+ gxl[i]*Y[:,i]
