from sklearn import datasets
from sklearn.linear_model import LinearRegression
loaded_data = datasets.load_boston()
#没有括号，都是属性，有括号是方法
data_X = loaded_data.data
data_y = loaded_data.target

model = LinearRegression()
model.fit(data_X,data_y)

print(model.coef_)
print(model.intercept_)
#输出{'copy_X': True, 'fit_intercept': True, 'n_jobs': 1, 'normalize': False}
print(model.get_params())
#对模型的拟合程度进行打分，输出为百分数
#score方法回归中是R^2,分类中是准 确度
print(model.score(data_X,data_y))