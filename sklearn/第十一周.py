import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.metrics import accuracy_score  as AC


def result(real, pred):
    from sklearn.metrics import confusion_matrix
    print(u"混淆矩阵")
    print(confusion_matrix(y_true=real, y_pred=pred))
    # from sklearn.metrics import accuracy_score  as AC  # 准确率是分类正确的样本占总样本个数的比例
    print("正确率：", AC(real, pred))
    # 如果正确率为一返回 i j k
    if AC(real, pred) == 1:
        print(i, j, k)
    from sklearn.metrics import precision_score  # 精确率指模型预测为正的样本中实际也为正的样本占被预测为正的样本的比例。
    print("精确率：", precision_score(real, pred, average=None))
    from sklearn.metrics import recall_score  # 召回率指实际为正的样本中被预测为正的样本所占实际为正的样本的比例。
    print("召回率", recall_score(real, pred, average=None))


# 导入数据
wine = datasets.load_digits()
wine_X = wine.data
wine_X = pd.DataFrame(wine_X)
wine_y = wine.target
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(wine_X, wine_y, test_size=0.1)
from sklearn.linear_model import LogisticRegression as LR

suanfa = ['liblinear', 'lbfgs', 'newton-cg', 'sag', 'saga']

for i in range(len(suanfa) - 1):
    for j in range(100, 1001, 100):
        for k in range(1000, 10000, 1000):
            lr = LR(C=j, random_state=k, solver=suanfa[i])
            lr.fit(x_train, y_train)
            R = lr.predict(x_test)
            result(y_test, R)
