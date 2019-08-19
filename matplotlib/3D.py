import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
#X,Y value
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
R = np.sqrt(X ** 2+Y ** 2)
#height value
Z = np.sin(R)
#rstride=rowStride,cstride=columnStride
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'),edgecolor='k')
#zdirection,z的话是压到Z轴的效果，x就是压倒X的效果，offset向下移两个单位
ax.contourf(X,Y,Z,zdir='y',offset=-4,cmap='rainbow')
ax.set_zlim(-2,2)
plt.show()