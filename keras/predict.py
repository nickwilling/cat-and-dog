import cv2
import  keras

CATEGORIES = ["Dog", "Cat"]

def prepare(filepath):
    IMG_SIZE = 50
    img_array = cv2.imread(filepath,cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
    #return的是keras要求的输入
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

model = keras.models.load_model("64x3-CNN.model")

#P.S.Predict always predict a list
prediction = model.predict([prepare('dog.jpg')])

print(prediction)
print(prediction[0])
print(prediction[0][0])
print(CATEGORIES[int(prediction[0][0])])