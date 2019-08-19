import matplotlib.pyplot as plt
import numpy as np

#figure就是一个大窗口
x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

plt.figure()
plt.plot(x,y2)
#figure plot第二条线,红色虚线
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
#x limit和y limit
plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('I am x')
plt.ylabel('I am y')
#设置坐标轴的单位小标
# new_ticks = np.linspace(-1,2,5)
# plt.xticks(new_ticks)
#坐标轴小标换成文字
plt.yticks([-2,-1.8,-1,1.23,3],['really bad','bad','normal','good','really good'])

#gca = 'get current axis'
ax = plt.gca()
#把上面和右面的轴设置为消失
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#设置下面的线为x轴，左边的线为y轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#x轴的position放在y轴的0点上
ax.spines['bottom'].set_position(('data',-0))# outward,axes
ax.spines['left'].set_position(('data',0))
plt.show()
