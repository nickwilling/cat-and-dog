import pandas as pd
import numpy as np
s = pd.Series([1,3,6,np.nan,44,1])
dates = pd.date_range('20190101',periods=6)
#dataFrame是一个行和列的Matrix，index是行的索引，columns是列的索引,默认是从0开始的数字
#np.random.randn是产生随机数，这些随机数是服从normal distribution的
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
print(df.columns)
#打印列
print(df['A'])
print("Unique",pd.unique(df['A']))

print(df.A)
#打印0-3行
print(df[0:3])
#打印所有行，A,B列,通过loc来打印
#loc查找的是标签的label，用0，1这种索引号是不行的，必须用label
#select by label:loc
print(df.loc[:,['A','B']])
print(df.loc['2019-01-02':'2019-01-04','A':'C'])


#iloc:indexLoc，就是用索引号来查找，不是标签
#select by position:iloc
print(df.iloc[0:3,0:3])
#选择不连续的数据
print(df.iloc[[1,3,5],0:3])

#选择筛选
#BooleanIndex
print(df[df.A > 8])