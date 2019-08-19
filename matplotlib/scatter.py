import matplotlib.pyplot as plt
import numpy as np

n = 1024
#numpy生成正态分布
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X) #for color value这里只是为了颜色好看
#size,color,alpha是transparent透明度
plt.scatter(X,Y,s=75,c=T,alpha=0.5)

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
#隐藏x和y的ticks，坐标轴的标度，就变成一张图片了，没有x和y轴
plt.xticks(())
plt.yticks(())
plt.show()