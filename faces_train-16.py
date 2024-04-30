import os
import cv2 as cv
import numpy as np

people=['modi','manav','elon']


# to store the training folders in a list
# p=[]
# for i in os.listdir(r'C:\Users\asus\Desktop\All\VS code\OpenCV\photos\Train'):
#     p.append(i)
# print(p)

DIR=r'C:\Users\asus\Desktop\All\VS code\OpenCV\photos\Train'

haar_cascade=cv.CascadeClassifier('haar_face.xml')

features=[]
labels=[]

def create_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path,img)

            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

            for(x,y,w,h) in faces_rect:
                face_roi = gray[y:y+h,x:x+w]         #faces region of interest
                features.append(face_roi)
                # if we choose manav the label would be 1 because it is in the oneth posistion at the index list
                labels.append(label)


create_train()
print('Training done-------------------')

features=np.array(features,dtype='object')
labels=np.array(labels)

# print(f'Length of the features={len(features)}')
# print(f'Length of the labels={len(labels)}')

face_recognizer=cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on the features list and the labels list
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')

np.save('features.npy',features)
np.save('Labels.npy',labels)