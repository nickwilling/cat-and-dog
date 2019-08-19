import pandas as pd
import numpy as np

dates = pd.date_range('20190101',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
#axis等于几就是对第几个维度进行操作
#axis=0就是列操作，就是上下操作
#axis=1就是行操作，就是左右操作
df.iloc[2,2] = 1111
print(df)
#把A列中大于4的值变成0,就对A进行操作
#df.A[df.A > 4] = 0
#如果A>4,就把对应的B中的数据改成0
df.B[df.A > 4] = 0
print(df)

#在df中新增一列空列df.F是没有用的，因为df中没有f这个属性
df['F'] = np.NAN
print(df)

