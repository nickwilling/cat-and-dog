import tensorflow as tf
import keras
from keras.callbacks import TensorBoard
from keras.models import  Sequential
from keras.layers import  Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle
import time

dense_layers = [0, 1, 2]
layer_sizes = [32, 64, 128]
conv_layers = [1, 2, 3]

X = pickle.load(open("X.pickle","rb"))
y = pickle.load(open("y.pickle","rb"))

#before we feed data through a neural network, normalize that data
#the easiest way to normalize data is going to be to scale that data
#in the image, the min=0 ,max=255,we can just do /255

X = X/255

#in model, the first layer needs to have a input shape, and the first dense layer has to have a flatten layer
for dense_layer in dense_layers:
    for layer_size in layer_sizes:
        for conv_layer in conv_layers:
            NAME = "{}-conv-{}-nodes-{}-dense-{}".format(conv_layer, layer_size, dense_layer, int(time.time()))
            tensorboard = TensorBoard(log_dir='logs/{}'.format(NAME))
            print(NAME)
            model = Sequential()
            model.add(Conv2D(layer_size,(3,3),activation='relu',input_shape = X.shape[1:]))
            model.add(MaxPooling2D(pool_size=(2,2)))

            for i in range(conv_layer-1):
                model.add(Conv2D(layer_size, (3, 3), activation='relu'))
                model.add(MaxPooling2D(pool_size=(2, 2)))

            model.add(Flatten())
            #before you do Dense, you have to flatten the data, cuz convolution is 2D, Dense layer id 1D

            for i in range(dense_layer):
                model.add(Dense(layer_size,activation='relu'))

            #当成二分类问题处理
            model.add(Dense(1,activation='sigmoid'))

            model.compile(loss=keras.losses.binary_crossentropy,optimizer='adam',metrics=['accuracy'])

            # Fraction of the training data to be used as validation data
            model.fit(X, y, batch_size=32, epochs=3, validation_split=0.1, callbacks=[tensorboard])
            model.save("{}.model".format(NAME))