import pandas as pd
import numpy as np

dates = pd.date_range('20190101',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan

#a[][]二维矩阵的第一个维度是行，第二个维度是列
#所以axis=0是是处理第一个维度，也就是行，axis=1时是第二个维度，也就是列
print(df.dropna(axis=0,how='any')) #how={any,all}any就是只要有一个是NAN就drop，all是这个行里所有的数据都是NAN才丢掉
print(df.dropna(axis=1,how='any'))

#把NAN的值都填充为0
print(df.fillna(value=0))


