#legend 图例，描述
import matplotlib.pyplot as plt
import numpy as np

#figure就是一个大窗口
x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

plt.figure(num=3,figsize=(8,5))
plt.plot(x,y2,label='up')
#figure plot第二条线,红色虚线
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down')
plt.legend(loc='best')
plt.show()
