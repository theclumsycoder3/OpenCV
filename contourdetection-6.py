import cv2 as cv
import numpy as np

img=cv.imread('Photos/dog4.jpg')
cv.imshow('Dog',img) 

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

'''blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny=cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)

contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

# RETR_TREE --> if you want all hierarchical contours
# RETR_EXTERNAL --> if you want only external contours
# RETR_LIST --> if you want all contours

# how we want to approximate the contour: 
# CHAIN_APPROX_NONE --> just returns all the contours
# CHAIN_APPROX_SIMPLE --> compresses all the contours that returned

'''
canny=cv.Canny(img,125,175)
cv.imshow('Canny Edges',canny)
contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

# Threshold--> binaries the image
# ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
# contours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# cv.imshow('Threshold',thresh)
print(f'{len(contours)} contour(s) found!')


# Draw Contours on blank screen
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Drawn',blank)

cv.waitKey(0)
