import numpy as np
import cv2 as cv

people=['modi','elon']
haar_cascade=cv.CascadeClassifier('haar_face.xml')

# features=np.load('features.npy', allow_pickle=True)
# labels=np.load('labels.npy')

face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img=cv.imread(r'C:\Users\asus\Desktop\All\VS code\OpenCV\photos\Train\modi\a2.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('PERSON',gray)


# first detect the face in the img
faces_rect=haar_cascade.detectMultiScale(gray,1.1,4)

for(x,y,w,h) in faces_rect:
    faces_roi=gray[y:y+h,x:x+w]

    label,confidence=face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0), thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Face',img)

cv.waitKey(0)
