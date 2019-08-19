# Arda Mavi
import cv2
import numpy as np
from os import listdir
from skimage import io
from scipy.misc import imresize
from keras.preprocessing.image import array_to_img, img_to_array, load_img



def get_img(data_path):
    # Getting image array from path:
    img_size = 64
    img = io.imread(data_path)
    #img=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    print("-----------------------")
    if len(img.shape)==2 :
        img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    img = imresize(img, (64, 64))
    print(img.shape)
    return img

def get_img_cutting(data_path):
    # Getting image array from path:
    #img_size = 64
    img = io.imread(data_path) 
    #src_RGB = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cutting = []
    cutting2 = []
    for j in range(3):  # [1]column-----------height  [2]column-----------width
            if j == 0:
                newpic = img[0:2048, 0:985]
                cutting.append(newpic)
            elif j == 1:
                newpic = img[0:2048, 985:1537]
                cutting.append(newpic)
            else:
                newpic = img[0:2048, 1537:2448]   
                cutting.append(newpic)
    for cut in cutting:
        pic = imresize(cut, (64, 64))
        if len(pic.shape)==2 :
            pic = cv2.cvtColor(pic, cv2.COLOR_GRAY2BGR)   
        cutting2.append(pic)  
    return cutting2

def get_dataset(dataset_path='Data/Train_Data'):
    # Getting all data from data path:
    try:
        X = np.load('Data/npy_train_data/X.npy')
        Y = np.load('Data/npy_train_data/Y.npy')
    except:
        labels = listdir(dataset_path) # Geting labels
        print('Categories:\n', labels)
        len_datas = 0
        for label in labels:
            len_datas += len(listdir(dataset_path+'/'+label))
        X = np.zeros((len_datas, 64, 64,3), dtype='float64')
        Y = np.zeros(len_datas)
        count_data = 0
        count_categori = [-1,''] # For encode labels
        for label in labels:
            datas_path = dataset_path+'/'+label
            for data in listdir(datas_path):
                pic = get_img(datas_path+'/'+data)
                X[count_data] = pic
            # For encode labels:
                if label != count_categori[1]:
                    count_categori[0] += 1
                    count_categori[1] = label
                Y[count_data] = count_categori[0]
                count_data += 1
        # Create dateset:
        import keras
        Y = keras.utils.to_categorical(Y)
        import os
        if not os.path.exists('Data/npy_train_data/'):
            os.makedirs('Data/npy_train_data/')
        np.save('Data/npy_train_data/X.npy', X)
        np.save('Data/npy_train_data/Y.npy', Y)
    from sklearn.model_selection import train_test_split
    X, X_test, Y, Y_test = train_test_split(X, Y, test_size=0.1, random_state=42)
    return X, X_test, Y, Y_test
