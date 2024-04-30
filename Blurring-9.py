import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

img=cv.imread('Photos/dog4.jpg')
cv.imshow('Dog',img)  

# First method of blurring--> Averaging
average=cv.blur(img,(3,3))  #(3,3)-> increase in kernel size leads to more blurring the img
cv.imshow('Average Blur',average)


#   Gaussian blur
gauss=cv.GaussianBlur(img,(3,3),0)   # here 0 is for standard deviation in x direction
cv.imshow('Gaussian Blur',gauss)


# Median Blur
median=cv.medianBlur(img,3) 
cv.imshow('Median Blur',median)

# Bilateral
bilateral =cv.bilateralFilter(img,10,35,25)    # 5 --> diameter ; 

# sigma color --> The value of sigma color. A larger value means that more color variation in the neighborhood will be considered while blurring, resulting in more pronounced blurring ;

# sigma space --> A larger value means that pixels farther away from the central pixel will influence the blurring more, resulting in a more pronounced effect.
cv.imshow('Bilateral blurring',bilateral)

cv.waitKey(0)