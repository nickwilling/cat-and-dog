import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#plot data

#Series:线性的数据：就是一维的数据
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
#累加
data = data.cumsum()

data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list("ABCD"))
data = data.cumsum()

ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class 1')
#ax=ax，这里的ax是指坐标系，如果用的坐标系是同一个的话那么就会画在同一个figure中。
data.plot.scatter(x='A',y='C',color='DarkGreen',label='Class 2',ax=ax)

plt.show()

