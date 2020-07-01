# -*- coding: utf-8 -*-
import pandas as pd
Data=pd.read_excel('农村居民人均可支配收入来源2016.xlsx')
X=Data.iloc[:,1:]
R=X.corr()

# 数据规范化处理
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X) 
X=scaler.transform(X)  

#主成分分析
from sklearn.decomposition import PCA
pca=PCA(n_components=0.90) 
pca.fit(X)
Y=pca.transform(X)
tzxl=pca.components_              
tz=pca.explained_variance_          
gxl=pca.explained_variance_ratio_   
Y00=sum(X[0,:]*tzxl[0,:])
Y01=sum(X[1,:]*tzxl[0,:])
Y02=sum(X[2,:]*tzxl[0,:])
Y03=sum(X[3,:]*tzxl[0,:])
print(X[0,:]*tzxl[0,:])
#综合排名
F=gxl[0]*Y[:,0]+gxl[1]*Y[:,1]+gxl[2]*Y[:,2] #综合得分=各个主成分*贡献率之和
dq=list(Data['地区'].values)  #提取地区
Rs=pd.Series(F,index=dq)           #以地区作为index，综合得分为值，构建序列
Rss=Rs.sort_values(ascending=False) #按综合得分降序进行排序

