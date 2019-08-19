#图中图
import matplotlib.pyplot as plt


fig = plt.figure()
x = [1,2,3,4,5,6,7]
y = [1,3,4,2,5,8,6]
left,bottom,width,height = 0.1,0.1,0.8,0.8
#坐标轴1是相对于整个figure，从左边0.1下面0.1为起点，宽度和高度为80%
ax1 = fig.add_axes([left,bottom,width,height])
ax1.plot(x,y,'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

#method 1:
left,bottom,width,height = 0.2,0.6,0.25,0.25
ax2 = fig.add_axes([left,bottom,width,height])
ax2.plot(y,x,'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title_insides_1')

#method 2：
plt.axes([.6,.2,.25,.25])
plt.plot(y[::-1],x,'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title_insides_2')


plt.show()
