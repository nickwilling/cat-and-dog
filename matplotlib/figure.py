import matplotlib.pyplot as plt
import numpy as np

#figure就是一个大窗口
x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

#plt.figure()是figure的开头，下面的都属于这张figure
plt.figure()
plt.plot(x,y1)

plt.figure(num=3,figsize=(8,5))
plt.plot(x,y2)
#figure plot第二条线,红色虚线
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.show()
