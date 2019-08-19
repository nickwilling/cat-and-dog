import pandas as pd
import numpy as np

#concatenating
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
df4 = pd.DataFrame(np.ones((3,4))*4,columns=['a','b','c','d'],index=[1,2,3])
df5 = pd.DataFrame(np.ones((3,4))*5,columns=['b','c','d','e'],index=[2,3,4])
#属性都是一样的，需要上下合并,会存在index重复的问题，可使用ignore_index
result = pd.concat([df1,df2,df3],axis=0,ignore_index=1)

#join内连接inner外连接outer，join进行左右合并
#列的并集是outer，交集是inner
res = pd.concat([df4,df5],join='inner',ignore_index=True)

#join_axes
#按照df4的index的顺序进行合并，将df5没有的用NaN进行填充，如果没有指定join_axes，则合并时行列都进行考虑
resu = pd.concat([df4,df5],axis=1,join_axes=[df4.index])

#append进行上下合并
resul = df1.append([df2,df3],ignore_index=True)

#添加行
s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res1 = df1.append(s1,ignore_index=True)
print(res1)