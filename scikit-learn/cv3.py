#这一节主要讲SVC（）中gamma参数变化的影响，选择gamma比较合适的模型以避免会引起过拟合的gamma同时loss又比较低
from  sklearn.model_selection import validation_curve
from sklearn.datasets import load_digits
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

digits = load_digits()
X = digits.data
y = digits.target
param_range = np.logspace(-6,-2.3,5)
train_loss,test_loss = validation_curve(SVC(),X,y,param_name='gamma',param_range=param_range,cv=10,
                                                  scoring='neg_mean_squared_error')
print(train_loss)
#axis=1代表跨行求均值。axis=0代表跨列求均值
train_loss_mean = -np.mean(train_loss,axis=1) #train loss多了一维，所以要加axis=1
test_loss_mean = -np.mean(test_loss,axis=1)

#这里的o-和x-代表每个节点的显示样式是圆圈⭕还是叉叉X
plt.plot(param_range,train_loss_mean,'o-',color='r',label="Training")
plt.plot(param_range,test_loss_mean,'x-',color="g",label="Cross-Validation")

plt.xlabel("gamma")
plt.ylabel("Loss")
#legend是右上角的注释
plt.legend(loc="best")
plt.show()