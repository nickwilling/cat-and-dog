import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
#uniform distribution均匀分布
Y1 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)
plt.bar(X,Y1,facecolor='#9999ff',edgecolor='black')
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')
#zip将X和Y1打包成元组
for x,y in zip(X,Y1):
    #ha:horizontal alignment横向对其方式
    plt.text(x,y+0.05,'%.2f' % y,ha='center',va='bottom')
for x,y in zip(X,Y2):
    #ha:horizontal alignment横向对其方式
    plt.text(x,-y-0.05,'%-.2f' % y,ha='center',va='top')
plt.xlim(-.5,n)
plt.ylim(-1.25,1.25)
plt.xticks(())
plt.yticks(())

plt.show()