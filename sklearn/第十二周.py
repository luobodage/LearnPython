import matplotlib.pyplot as plt
from sklearn import datasets  # 自带数据集

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def result(real, pred):
    from sklearn.metrics import confusion_matrix
    print(u"混淆矩阵")
    print(confusion_matrix(y_true=real, y_pred=pred))
    from sklearn.metrics import accuracy_score  as AC  # 准确率是分类正确的样本占总样本个数的比例
    print("正确率：", AC(real, pred))
    from sklearn.metrics import precision_score  # 精确率指模型预测为正的样本中实际也为正的样本占被预测为正的样本的比例。
    print("精确率：", precision_score(real, pred, average=None))
    from sklearn.metrics import recall_score  # 召回率指实际为正的样本中被预测为正的样本所占实际为正的样本的比例。
    print("召回率", recall_score(real, pred, average=None))


cancer = datasets.load_breast_cancer()

x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=66)
knn = KNeighborsClassifier(3)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
result(y_test, y_pred)