from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X = iris.data
y = iris.target



# #random_state:随机种子，限定这个值后每次得到的随机结果都是一样的，用来复现数据
# X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=4)
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(X_train,y_train)
# y_pred = knn.predict(X_test)
# print(knn.score(X_test,y_test))

#选择N
from sklearn.model_selection import  cross_val_score
import matplotlib.pyplot as plt
k_range = range(1,31)
k_scores = []
k_loss = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    # 将X和y自动分成5组，fit和score只是一组数据，70%用来train,30%用来test
    # scoring参数指定评价函数，例如：accuracy， roc_auc等
    # estimator : estimator object implementing 'fit' The object to use to fit the data.
    scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')  # for classification accuray用于分类问题
    loss = -cross_val_score(knn,X,y,cv=10,scoring='neg_mean_squared_error')  # for regression MSE用于回归
    k_scores.append(scores.mean())
    k_loss.append(loss.mean())
plt.plot(k_range,k_scores)
plt.plot(k_range,k_loss)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
plt.show()
