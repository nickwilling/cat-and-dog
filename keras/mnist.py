import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Flatten,Dense
import matplotlib.pyplot as plt
#print(tf.__version__) the version of tensorflow
mnist = keras.datasets.mnist # 28*28 image of hand-written digits 0-9
#unpack it to training dataset and test dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#once we have data, we want to normalize it,and the pic of 5 change a little bit, a little lighter
#没有normalize的时候每个像素点的值是0-255，normalize以后变成了0-1，make it easier for network to learn
#normalize 以后对神经网络的影响非常大。
x_train = keras.utils.normalize(x_train, axis=1)
x_test = keras.utils.normalize(x_test, axis=1)

#build the model
#Sequential model是feed-forward的
#define the Architecture of the model
#the first layer is input layer
#输入的图片是28*28的multi-dimension array，但模型需要Flat
model = Sequential()
model.add(Flatten())#输入层应该是是Flatten的，后面才能加全连接层
model.add(Dense(128,activation=tf.nn.relu))
model.add(Dense(128,activation=tf.nn.relu))
model.add(Dense(10,activation=tf.nn.softmax))#到这里模型就定义完了

model.compile(optimizer='adam',
              loss=keras.losses.sparse_categorical_crossentropy,
              metrics=['accuracy'])

#ready to train the model
model.fit(x_train,y_train,epochs=3)

#A model can easily be overfit,so we need to calculate the validation loss and accuracy
val_loss, val_acc = model.evaluate(x_test,y_test)
print(val_loss,val_acc)

#save model
model.save('epic_num_reader.model')

#read mmodel
new_model = keras.models.load_model('epic_num_reader.model')

#make predictions
predictions = new_model.predict(x_test)

import numpy as np
print(np.argmax(predictions[0]))

plt.imshow(x_test[0])
plt.show()


# #see what the data is
# import matplotlib.pyplot as plt
#
# plt.imshow(x_train[0],cmap = plt.cm.binary)#cmap和cm都是color map
# plt.show()




