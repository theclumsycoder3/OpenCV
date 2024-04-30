import cv2 as cv

img1 = cv.imread('photos/dog3.jpg')
cv.imshow('dog3', img1) 
def rescaleFrame(frame,scale=0.5):
    # this method will work for Images,Videos and Live Videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img1 = cv.imread('photos/dog3.jpg')
cv.imshow('dog3', img1) 
resize_img1 = rescaleFrame(img1)
cv.imshow('Image', resize_img1)

# converting imgae to grayscale
# gray=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# blur an image
blur=cv.GaussianBlur(resize_img1,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Find Edge Cascade  --> we can reduce the edges by blurring the image
# canny=cv.Canny(img1,125,175)
# cv.imshow('Canny Edges',canny)
canny=cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)

# how to dilate the image
dilated=cv.dilate(canny,(7,7),iterations=1)
cv.imshow('Dialated',dilated)

# Eroding
eroded=cv.erode(dilated,(7,7),iterations=1)
cv.imshow('Eroded',eroded)

# Resize and crop img
resized=cv.resize(resize_img1,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resized',resized)

# Cropping
cropped=resize_img1[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)