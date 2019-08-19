#在一个figure里创建多个小图（Subplot）
import matplotlib.pyplot as plt

plt.figure()

#两行两列第一个位置
plt.subplot(2,2,1)
plt.plot([0,1],[0,1])

plt.subplot(2,2,2)
plt.plot([0,1],[0,2])

plt.subplot(2,2,3)
plt.plot([0,1],[0,3])

plt.subplot(2,2,4)
plt.plot([0,1],[0,4])

plt.figure()
#两行1列，第一个图占一行
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])
#第二行是两行三列
plt.subplot(2,3,4)
plt.plot([0,1],[0,2])

plt.subplot(2,3,5)
plt.plot([0,1],[0,3])

plt.subplot(2,3,6)
plt.plot([0,1],[0,4])

plt.show()