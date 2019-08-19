# Arda Mavi

from keras.models import Sequential
from keras.models import model_from_json
import math
from get_dataset import get_img_cutting
from get_dataset import get_img
import tensorflow as tf
import os
import numpy as np
    # Getting model:
model_file =open('Data/Model/model.json', 'r')
model = model_file.read()
model_file.close()
model = model_from_json(model)
    # Getting weights
model.load_weights("Data/Model/weights.h5")
img = [];
path1 = "product/"
# with open('test.txt', 'w') as f:
#     for lists in os.listdir(path1):
# #如果找到的是图片，则打印出来
#         if lists[-3:]=='jpg':
#             img_dir = os.path.join(path1, lists)
#             img = get_img_cutting(img_dir)
#         count = 0
#         for cutting in img:
#             X = np.zeros((1, 64, 64,3), dtype='float64')
#             X[0] = cutting
#             if model.predict(X)[0][0]>model.predict(X)[0][1] :
#                 f.write("0 ")
#             else:
#                 f.write("1 ")
#                 count = count + 1
#         print(count)
#         if(count==3):
#             f.write("合格"+'\n')
#         else :
#             f.write("不合格"+'\n')
#             continue
#
from PIL import Image
import matplotlib.pyplot as plt
from scipy.misc import imresize
img=Image.open('D:\cat-and-dog\product\green.jpg')
pic = imresize(img, (64, 64))
X = np.zeros((1, 64, 64,3), dtype='float64')

X[0] = pic
y = model.predict(X)
print("this is y",y)
if np.argmax(y,1)==0:
    print('该区域为绿灯！')
elif np.argmax(y,1)==1:
    print('该区域为红灯！')
else:
    print('该区域为黄灯！')

    

plt.figure("green")
plt.imshow(img)
plt.show()
   
    
