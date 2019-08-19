from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
wine = load_wine()
#通过pandas看一下wine数据集是什么样的
#wine的X有13个特征，3个标签
# import pandas as pd
# print(pd.concat([pd.DataFrame(wine.data),pd.DataFrame(wine.target)],axis=1))
# #打印特征的名字
# print(wine.feature_names)
# #打印标签的名字
# print(wine.target_names)
#train_test_split加上random_state以后生成的样本集的顺序就固定下来了，每次调用都产生一样的结果
X_train, X_test, y_train, y_test = train_test_split(wine.data,wine.target,test_size=0.3,random_state=4)

#建模。
#生成树前，splitter可以防止过拟合，树生成以后也还是可以通过剪枝来处理过拟合
# clf = tree.DecisionTreeClassifier(criterion='entropy'
#                                   # ,max_depth=3  #max和min用来剪枝
#                                   # ,min_samples_leaf=10
#                                   # ,min_samples_split=10 #只有你的样本大于这个值的时候才可以去分割，不然就剪掉
#                                   # ,random_state=30 #不加random_state每次执行的score都是不一样了，加了以后可以把score固定下来，相当于随机选择的时候每次都选一条路
#                                   # ,splitter='best'
#                                 )
# clf = clf.fit(X_train,y_train)
# score = clf.score(X_test,y_test)
# print(score)

#画树
# import graphviz
# feature_names = ['酒精','苹果酸','灰','灰的碱性','镁','总酚','类黄酮','非黄烷类酚类','花青素','颜色强度','色调','od280/od315稀释葡萄酒','脯氨酸']
#
# dot_data = tree.export_graphviz(clf,out_file=None,feature_names=wine.feature_names,
#                                 class_names=["qinjiu","xueli","beiermode"],
#                                 filled=True,
#                                 rounded=True,
#                                 special_characters=True)
# graph = graphviz.Source(dot_data)
#
# graph.render("tree")

#打印各个特征的重要性
# z = zip(feature_names,clf.feature_importances_)
# for f,i in z:
#     print(f,i)
#
# print([*zip(feature_names,clf.feature_importances_)])

#确定参数，超参数的取值
import matplotlib.pyplot as plt

test = []
for i in range(10):
    clf = tree.DecisionTreeClassifier(max_depth=i+1
                                      ,criterion='entropy'
                                      ,random_state=30)
    clf = clf.fit(X_train,y_train)
    score = clf.score(X_test,y_test)
    test.append(score)
plt.plot(range(1,11),test,color='red',label="max_depth")
plt.legend()
plt.show()

#apply 返回每个测试样本所在的叶子节点的索引
clf.apply(X_test)

clf.predict(X_test)