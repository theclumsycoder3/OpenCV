import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

img=cv.imread('Photos/dog4.jpg')
cv.imshow('Dog',img) 

# plt.imshow(img)
# plt.show()


# BGR to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# BGR to L*a*b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('Lab',lab)

# BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

# grayscale to BGR
gray_bgr=cv.cvtColor(img,cv.COLOR_GRAY2BGR)
cv.imshow('Gray --> BGR',gray_bgr)

# HSV to BGR
hsv_bgr=cv.cvtColor(img,cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR',hsv_bgr)

# L*a*b to BGR
lab_bgr=cv.cvtColor(img,cv.COLOR_LAB2BGR)
cv.imshow('Lab --> BGR',lab_bgr)

# RGB to BGR
rgb_bgr=cv.cvtColor(img,cv.COLOR_RGB2BGR)
cv.imshow('RGB --> BGR',rgb_bgr)



plt.imshow(rgb)
plt.show()

cv.waitKey(0)