import cv2 as cv


# reading images
img1 = cv.imread('photos/dog1.jpg')
cv.imshow('dog1', img1)  


# reading videos
# capture =cv.VideoCapture(0)   --> for webcam
capture =cv.VideoCapture('videos/doggie1.mp4')

while True:
    ifTrue,frame=capture.read()
    cv.imshow('video',frame)

    # waitkey() function --> allows users to display a window for given milliseconds or until any key is pressed

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()



