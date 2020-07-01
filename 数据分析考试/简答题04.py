from sklearn import datasets
from sklearn.model_selection import train_test_split,cross_val_score
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
from sklearn.linear_model import LogisticRegression as LR
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(iris_X)
X = scaler.transform(iris_X)
from sklearn.decomposition import PCA
pca = PCA(0.85)
pca.fit(X)
Y = pca.transform(X)
X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.1)
lr1 = LR()
score = cross_val_score(pca,iris_X,iris_y,cv=5)
print(score)

