from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import  train_test_split
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
import matplotlib.pyplot as plt
# a = np.array([[10,2.7,3.6],
#               [-100,5,-2],
#               [120,20,40]],dtype=np.float64)
#
# print(a)
# #在sci-kit中normalization就是scale，因为属性值之间的差别会很大，normalize以后属性的取值范围都差不多，更适合机器去学习
# print(preprocessing.scale(a))

X,y = make_classification(n_samples=300,n_features=2,n_redundant=0,n_informative=2,
                          random_state=22,n_clusters_per_class=1,scale=100)
#这里的c是clor，用y的值来区分深浅度
plt.scatter(X[:,0],X[:,1],c=y)
plt.show()

#scale以前准确率是52，scale之后准确率是93，由此可见normalization还是很重要的
X = preprocessing.minmax_scale(X,feature_range=(-1,1))
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.3)
clf = SVC()
clf.fit(X_train,y_train)
print(clf.score(X_test,y_test))
