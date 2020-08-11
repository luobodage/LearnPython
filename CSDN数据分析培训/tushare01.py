import numpy as np
import pandas as pd

# 删除，，填充，，，插值，这是我们处理缺失值常用的方法

# 加载数据
data = [
    [25698744, 5145, 444],
    [np.nan, np.nan, 445],
    [25698746, 5156, np.nan],
    [25698747, np.nan, 447],
    [np.nan, 5145, 448],
    [25698749, np.nan, '*'],
    [25698743, 5454, 450]
]
data = pd.DataFrame(data, columns=['商品id', '类别id', '门店编号'])

# 检测缺失值
print(data.isnull())  # True表示缺失值
print(data.notnull())  # Flase表示缺失值

# 统计缺失值
# sum 统计的是true 所以建议使用isnull
print(data.isnull().sum())
print(data.notnull().sum())

# 缺失值的处理
# 删除 ----会对数据产生很大的影响，造成数据缺失，所以在数据大部分为缺失值，才使用删除法
# axis=【行0列1】
# how=【删除方式，any=只要有缺失值，就删除[整行或者整列]，all=只有整列或者整行都是缺失值，才删除】
# inplace=【是否影响原数据】
data.dropna(axis=1, how='any', inplace=True)
print(data)

# 填充  --- 填充之后对结果影响不大的情况，可以使用
# 为了对整体的数据不产生影响，，一般使用 --- 均值，中位数，众数【类别型数据】来进行填充
# 众数
mode = data.loc[:, '商品ID'].mode()[0]
data.loc[:, '商品ID'].fillna(value=mode, inplace=True)
mode = data.loc[:, '类别ID'].mode()[0]
data.loc[:, '类别ID'].fillna(value=mode, inplace=True)
mode = data.loc[:, '门店编号'].mode()[0]
data.loc[:, '门店编号'].fillna(value=mode, inplace=True)
print(data)

print('-*' * 40)
# 对于一些非空值的特殊符号的处理
# 先将其转化为缺失值，在进行处理
data.replace(to_replace='*', value=np.nan, inplace=True)
mode = data.loc[:, '门店编号'].mode()[0]
data.loc[:, '门店编号'].fillna(value=mode, inplace=True)
print(data)

# 插值
x = np.array([1, 2, 3, 4, 5, 8, 9])
y = np.array([3, 5, 7, 9, 11, 17, 19])
z = np.array([2, 8, 18, 32, 50, 128, 162])

# 线性插值，多项式插值，样条插值
# 线性插值 -- 拟合线性关系进行插值
from scipy.interpolate import interp1d

line1 = interp1d(x, y, kind='linear')
line2 = interp1d(x, z, kind='linear')
print(line1([6, 7]))  # [13. 15.]
print(line2([6, 7]))  # [ 76. 102.]

# 多项式插值 -- 牛顿插值法，拉格朗日插值法
# 拟合牛顿多项式 与 拉格朗日多项式
from scipy.interpolate import lagrange

la1 = lagrange(x, y)
la2 = lagrange(x, z)
print(la1([6, 7]))  # [13. 15.]
print(la2([6, 7]))  # [72. 98.]

# 样条插值 -- 拟合曲线关系进行插值
from scipy.interpolate import spline

print(spline(xk=x, yk=y, xnew=np.array([6, 7])))  # [ 13.  15.]
print(spline(xk=x, yk=z, xnew=np.array([6, 7])))  # [ 72.  98.]

# 对于线性关系的数据 ---线性插值比较准确，多项式插值与 样条插值都不错，
# 如果是线性关系的数据----都可以使用

# 对于非线性数据---线性插值效果较差，多项式插值与样条插值效果较好，
# 如果是非线性关系的数据，---推荐使用多项式插值与样条插值