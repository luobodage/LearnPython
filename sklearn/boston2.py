import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
# 将数据一分为二
from sklearn.model_selection import train_test_split
# 均方误差
from sklearn.metrics import mean_squared_error
import pandas as pd
from sklearn import datasets

fj = datasets.load_boston()


print(type(fj))
data1 = pd.DataFrame(data= np.c_[fj['data'], fj['target']],
                     columns= fj['feature_names'] + ['target'])
# 加载数据
# 加载训练数据
# train = pd.read_table('./zhengqi_train.txt') 和下面一行的效果相同
train = fj
train
# 加载测试数据
test = fj
test


# 将训练数据分乘特征值和目标值
# 特征, 影响目标值的因素
X = train[:, :-1]
# 目标值
y = train['target']

# 算法评估, 将上面的数据分成两份,一部分用来训练, 一部分用来测试
X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size = 0.2)


# 使用普通线性回归模型
linear = LinearRegression()
linear.fit(X_train, y_train)
y_ = linear.predict(X_validation)
mean_squared_error(y_validation,y_)   # 均方误差
'''0.11713370444738197'''

# 使用线性模型预测测试数据
y_commit = linear.predict(test)
# 保存数据到本地
s = pd.Series(y_commit)
s.to_csv('./linear_result.txt', index=False, header = False)


# 使用岭回归模型
ridge = Ridge(alpha=256)   # alpha值
ridge.fit(X_train, y_train)
y_ = ridge.predict(X_validation)
mean_squared_error(y_validation,y_)
'''0.13427749653218798'''

y_commit = ridge.predict(test)
pd.Series(y_commit).to_csv('./ridge_result.txt', index=False, header = False)
