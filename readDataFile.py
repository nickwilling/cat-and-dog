import pickle
import matplotlib.pyplot as plt
import cv2
#read data From RGB color
pickle_in = open("XRGB.pickle","rb")
X = pickle.load(pickle_in)
pickle_in.close()

pickle_in = open("yRGB.pickle","rb")
y = pickle.load(pickle_in)
pickle_in.close()

#read data From Gray color
pickle_in = open("X.pickle","rb")
X1 = pickle.load(pickle_in)
pickle_in.close()

pickle_in = open("y.pickle","rb")
y1 = pickle.load(pickle_in)
pickle_in.close()

plt.imshow(X[0])
plt.show()

img = cv2.resize(X1[0],(50,50))
img2 = cv2.resize(X[0],(50,50))
print("the shape of img is "+str(img.shape))
print("the shape of img2 is "+str(img2.shape))
plt.imshow(img,cmap="gray")
plt.show()
print(X[0].shape)
print(y[0])
print(X1[0].shape)
print(y1[0])
