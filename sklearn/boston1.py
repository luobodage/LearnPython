import pandas as pd
import numpy  as np
from sklearn import datasets

boston_data = datasets.load_boston()
df_boston = pd.DataFrame(boston_data.data,columns=boston_data.feature_names)
df_boston['target'] = pd.Series(boston_data.target)
df_boston.head()

def sklearn_to_df(sklearn_dataset):
    df = pd.DataFrame(sklearn_dataset.data, columns=sklearn_dataset.feature_names)
    df['target'] = pd.Series(sklearn_dataset.target)
    return df

df_boston = sklearn_to_df(datasets.load_boston())
x = df_boston.iloc[:,0:4]
y = df_boston.iloc[:,4]


x = x.values
y = y.values
# 2.导入线性回归模块，简称为LR
from sklearn.linear_model import LinearRegression as LR

lr = LR()  # 创建线性回归模型类
lr.fit(x, y)  # 拟合  训练  a b c d e
#  基准数据
Slr = lr.score(x, y)

# 岭回归  套索回归
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso  # 减少训练集的个数
# =============================================================================
# a = np.zeros(100)
# c = np.zeros(100)
# b = np.arange(0,100,1)
# for i in b:
#     rlr = Ridge(alpha=i)   # float
#     rlr.fit(x,y)
#     srlr = rlr.score(x,y)
#     a[i] = srlr - Slr
#
#     llr = Lasso(i)
#     llr.fit(x,y)
#     sllr = llr.score(x,y)
#     c[i] = sllr - Slr
# maxa = a.max()
# maxc = c.max()
#
# =============================================================================


# 对数据进行规格化处理

# 数据规格化
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaler.fit(x)
X = scaler.transform(x)
stdlr = LR()
stdlr.fit(X, y)
Sstdlr = stdlr.score(X, y)

# 岭回归  套索回归
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

a = np.zeros(100)
c = np.zeros(100)
b = np.arange(-100, 100, 2)
for i in b:
    rlr = Ridge(alpha=i)
    rlr.fit(X, y)
    srlr = rlr.score(X, y)
    a[i] = srlr - Slr

    llr = Lasso(i)
    llr.fit(X, y)
    sllr = llr.score(X, y)
    c[i] = sllr - Slr
maxa = a.max()
maxc = c.max()