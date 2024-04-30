import cv2 as cv

# resizing and rescaling frames and images
def rescaleFrame(frame,scale=0.2):
    # this method will work for Images,Videos and Live Videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# reading images
img1 = cv.imread('photos/dog1.jpg')
cv.imshow('dog1', img1)  
# resize img
resize_img1 = rescaleFrame(img1)
cv.imshow('Image', resize_img1)


# reading videos
# capture =cv.VideoCapture(0)   --> for webcam
capture =cv.VideoCapture('videos/doggie1.mp4')

while True:
    ifTrue,frame=capture.read()

    frame_resized=rescaleFrame(frame)

    cv.imshow('video',frame)

    cv.imshow('video resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

# another way of resizing specific for videos
def changeRes(width,height):
    # only for LIVE VIDEO--> videos reading from external camera or webcam
    capture.set(3,width)
    capture.set(4,height)

