import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets  # 导入数据集
from matplotlib.colors import ListedColormap
from sklearn import svm  # sklearn 自带 SVM 分类器

# 设置颜色
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

# 导入鸢尾花（Iris）数据集
iris = datasets.load_iris()
X = iris.data[:, 0:2]  # 取数据集前两列特征向量
Y = iris.target  # 取数据集的标签（鸢尾花类型）

clf = svm.SVC()  # 创建 SVM 分类起
clf.fit(X, Y)  # 拟合数据

# 设置 X、Y 轴
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max), np.arange(y_min, y_max))

# 绘制网格上每个数据点的决策函数
wyd = np.c_[xx.ravel(), yy.ravel()]
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=cmap_bold, edgecolors='k', s=30)

plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.show()