import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

img=cv.imread('Photos/city.jpg')
cv.imshow('City',img)  

# dimensions of the mask has to be same size of the image if not its not gonna work
blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank Image',blank)

mask=cv.circle(blank,(img.shape[1]//2+45, img.shape[0]//2+45),100,255,-1)      #it is of a circle
mask=cv.rectangle(blank,(img.shape[1]//2, img.shape[0]//2),(img.shape[1]//2+100, img.shape[0]//2+100),255,-1)
cv.imshow('Mask',mask)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked img',masked)

cv.waitKey(0)