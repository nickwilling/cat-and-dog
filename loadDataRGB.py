import numpy as np
import  matplotlib.pyplot as plt
import os
import cv2

DATADIR = "F:\kagglecatsanddogs\PetImages"
CATEGORIES = ["Dog", "Cat"]

IMG_SIZE = 50

#create training data
training_data = []
def create_training_data():
    # read imgs from file
     for category in CATEGORIES:
        path = os.path.join(DATADIR, category)  # path to cats or dogs dir
        class_num = CATEGORIES.index(category)  #we need the digital class(label) not the string class
        for img in os.listdir(path):
            #读文件的时候可能会碰到图片损坏或者OS error和其他的error，就PASS
            try:
                # RGB data is 3 times the size of grayscale data, and color is not essential in this specific task
                img_array = cv2.imread(os.path.join(path, img))  # full dir+name
                # make every data the same shape
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array,class_num])
            except Exception as e:
                pass

create_training_data()
print(len(training_data))

#训练集中最好所有的类别都是50%-50%。不然如果狗是75%，
# 猫是25%，那么只要碰到一张图片就predict Dog，也会有75%的准确率

#得到了training data以后要打乱顺序
#shuffle the data
import  random
random.shuffle(training_data)

#X is feature set, y is labels
X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

#必须要把X reshape成NN可以接受的输入
X = np.array(X).reshape(-1,IMG_SIZE,IMG_SIZE,3)

#save your data， so you don't have to create it every time
import pickle
pickle_out = open("XRGB.pickle","wb")
pickle.dump(X,pickle_out)
pickle_out.close()

pickle_out = open("yRGB.pickle","wb")
pickle.dump(y,pickle_out)
pickle_out.close()

#read data
pickle_in = open("XRGB.pickle","rb")
X = pickle.load(pickle_in)
pickle_in.close()

pickle_in = open("yRGB.pickle","rb")
y = pickle.load(pickle_in)
pickle_in.close()

print(X[0])
print(y[0])