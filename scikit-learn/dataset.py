from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# loaded_data = datasets.load_boston()
# #没有括号，都是属性，有括号是方法
# data_X = loaded_data.data
# data_y = loaded_data.target
#
# model = LinearRegression()
# model.fit(data_X,data_y)
#
# print(model.predict(data_X[:4]))
# print(data_y[:4])

#noise变大的话，点会更加离散
X,y = datasets.make_regression(n_samples=100,n_features=1,n_targets=1,noise=1)
plt.scatter(X,y)
plt.show()


