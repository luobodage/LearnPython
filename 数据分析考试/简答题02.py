from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target

X_train,X_test,y_train,y_test = train_test_split(data_X,data_y,test_size=0.3)
model = LinearRegression()
model.fit(X_train,y_train)
result = model.predict(X_test)
print(result)