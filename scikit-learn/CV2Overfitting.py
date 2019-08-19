from  sklearn.model_selection import learning_curve
from sklearn.datasets import load_digits
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

digits = load_digits()
X = digits.data
y = digits.target

train_sizes,train_loss,test_loss = learning_curve(SVC(gamma=0.001),X,y,cv=10,
                                                  scoring='neg_mean_squared_error',train_sizes=[0.1,0.25,0.5,0.75,1])
print(train_loss)
#axis=1代表跨行求均值。axis=0代表跨列求均值
train_loss_mean = -np.mean(train_loss,axis=1) #train loss多了一维，所以要加axis=1
test_loss_mean = -np.mean(test_loss,axis=1)

#这里的o-和x-代表每个节点的显示样式是圆圈⭕还是叉叉X
plt.plot(train_sizes,train_loss_mean,'o-',color='r',label="Training")
plt.plot(train_sizes,test_loss_mean,'x-',color="g",label="Cross-Validation")

plt.xlabel("Training examples")
plt.ylabel("Loss")
#legend是右上角的注释
plt.legend(loc="best")
plt.show()