import pandas as pd
import numpy as np

data = pd.read_excel('credit.xlsx')  # 取数据集
x = data.iloc[:600, :14].as_matrix()  # 训练集x  x_train,
y = data.iloc[:600, 14].as_matrix()  # 训练集y  y_train

x1 = data.iloc[600:, :14].as_matrix()  # 测试集X   ,x_test
y1 = data.iloc[600:, 14].as_matrix()  # 测试集y  y_test

from sklearn.linear_model import LogisticRegression as LR

lr = LR()  # 创建逻辑回归模型类
lr.fit(x, y)  # 训练数据
r = lr.score(x, y);  # 模型准确率（针对训练数据）
R = lr.predict(x1)  # 用训练的结果预测对 测试集X  进行预测
Z = R - y1
Rs = len(Z[Z == 0]) / len(Z)  # 预测效果
print('预测结果为：', R)
print('预测准确率为：', Rs)

# 数据规格化
from sklearn.preprocessing import StandardScaler

xa = data.iloc[:, :14].as_matrix()  # 取 X
ya = data.iloc[:, 14].as_matrix()  # 取 y

scaler = StandardScaler()
scaler.fit(xa)

X = scaler.transform(xa)  # X  标准化后的结果
# 主成分分析
from sklearn.decomposition import PCA

pca = PCA(0.85)  # 定义实例  0.85
pca.fit(X)
Y = pca.transform(X)  # Y降维之后的结果

from sklearn.model_selection import train_test_split

xa = pd.DataFrame(Y)
yy = pd.DataFrame(ya)
x_train, x_test, y_train, y_test = train_test_split(xa, yy, test_size=0.3)  # 随机拆分
# =============================================================================
# x_train = xa.iloc[:600,:].as_matrix()
# x_test = xa.iloc[600:,:].as_matrix()
# y_train = yy.iloc[:600,:].as_matrix()
# y_test = yy.iloc[600:,:].as_matrix()
# =============================================================================


lr1 = LR()  # 创建逻辑回归模型类
lr1.fit(x_train, y_train)  # 训练数据
r1 = lr1.score(x_train, y_train);  # 模型准确率（针对训练数据）
R1 = lr1.predict(x_test)
pp = y_test.values

zzz = pp.ravel()
Z1 = R1 - zzz
Rs1 = len(Z1[Z1 == 0]) / len(Z1)
