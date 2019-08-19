import pandas as pd

#因为字典是无序的，所以Key在AB后面
#merging two df by key/keys
left = pd.DataFrame({'Key':['K0','K1','K2','K3'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})

right = pd.DataFrame({'Key':['K0','K1','K2','K3'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})

res = pd.merge(left,right,on='Key')

#consider two keys
#Key1和Key2一起看，然后合并
#内连接中只考虑相同的Key，left1先看是K0,K0，right1里面有一样的，就复制下来，left1里K0，K1，r里没有，就不复制，l1里K1，K0，r里有两个，就把这两个都复制下来
#外连接中不管Key一不一样都要复制下来（并），没有的数据就用NaN代替
#左连接，外连接中左边走下来
#右连接，外连接中右边走下来
left1 = pd.DataFrame({'Key1':['K0','K0','K1','K2'],
                      'Key2':['K0','K1','K0','K1'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})

right1 = pd.DataFrame({'Key1':['K0','K1','K1','K2'],
                     'Key2':['K0','K0','K0','K0'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})
print(left1)
print(right1)

res1 = pd.merge(left1,right1,on=['Key1','Key2'],how='right')
print(res1)