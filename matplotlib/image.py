import matplotlib.pyplot as plt
import numpy as np

#图片其实就是X和Y轴每个点有一个数值，这个数值对应到colormap里有一个颜色，组合起来就是一张图片
# image data
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)

#origin=lower图片会上下颠倒
# plt.imshow(a,interpolation='gaussian',cmap='bone',origin='lower')
plt.imshow(a,interpolation='nearest',cmap='bone',origin='lower')
plt.colorbar(shrink=0.9)
plt.show()