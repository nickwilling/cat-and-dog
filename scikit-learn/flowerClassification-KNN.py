import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

#:是全部的意思，第一个冒号是选择前两行所有的，第二个冒号是选择所有列
# print(iris_X[:2,:])
# print(iris_y)

#split the data into train and test data, shuffle the data
#乱的数据永远比不乱的数据更好
X_train,X_test,y_train,y_test = train_test_split(iris_X,iris_y,test_size=0.3)

# print(y_train)
# print(y_train)

knn = KNeighborsClassifier()
knn.fit(X_train,y_train)

print(knn.predict(X_test))
print(y_test)