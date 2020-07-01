from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

digits = datasets.load_digits()

data = digits.data
target = digits.target
X_train,X_test,y_train,y_test = train_test_split(data,target,test_size=0.25)
clf = KNeighborsClassifier()
clf.fit(X_train,y_train)
Z = clf.predict(X_test)
print(Z)