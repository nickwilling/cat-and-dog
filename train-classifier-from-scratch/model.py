import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import data_preprocessing
import keras
from keras.models import Sequential
from keras.layers import Flatten,Dense
data = data_preprocessing.load_data(download=False)
new_data = data_preprocessing.convert2onehot(data)

#convert DataFrame to Numpy
new_data = new_data.values.astype(np.float32)

print(new_data.shape)
#数据在训练的时候需要被打乱顺序
np.random.shuffle(new_data)

#打乱顺序以后就要分开所有的数据
#设定分离的索引点
sep = int(0.7*len(new_data))
train_data = new_data[:sep]#70% training data
test_data = new_data[sep:]#30% test data
print(new_data.shape)
x_train = train_data[:,:21]
y_train = train_data[:,21:]
x_test,y_test = test_data[:,:21],test_data[:,21:]
print(x_train.shape)
print(y_train.shape)
print(x_train.shape[0:1])
print("1111111111111111",x_train.shape[0:1])
model = Sequential()
model.add(Flatten())#输入层应该是是Flatten的，后面才能加全连接层
model.add(Dense(128,activation=tf.nn.relu,input_shape=x_train.shape[0:1]))
model.add(Dense(128,activation=tf.nn.relu))
model.add(Dense(4,activation=tf.nn.softmax))#到这里模型就定义完了

model.compile(optimizer='adam',
              loss=keras.losses.categorical_crossentropy,
              metrics=['accuracy'])

model.fit(x_train.reshape(len(x_train),21,1),y_train,epochs=20)

val_loss, val_acc = model.evaluate(x_test.reshape(len(x_test),21,1),y_test)
print(val_loss,val_acc)

test = [0,0,0,1,0,0,1,0,1,0,0,0,0,0,1,1,0,0,0,0,1]
test = np.array(test).reshape(1,21,1)
prediction = model.predict([test])
print(np.argmax(prediction))

model.save('car_classifier.model')

