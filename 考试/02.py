import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import cross_val_score

iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                                    test_size=0.4, random_state=0)
print(iris.data.shape, iris.target.shape)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
score = clf.score(X_test, y_test)
print('Accuracy:', score)

iris = datasets.load_iris()
scores = cross_val_score(clf, iris.data, iris.target, cv=5)
print('5折结果为:', scores)
print("Accuracy: ", scores.mean())
