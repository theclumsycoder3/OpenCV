import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')  #unit8 is a datatype of image
cv.imshow('Blank', blank)  

# img1 = cv.imread('photos/dog1.jpg')
# cv.imshow('Dog', img1)  


# 1. paint the image a certain colour

# blank[:]=0,0,255
# cv.imshow('Red', blank) 

# color certain portion
# blank[200:300,300:400]=0,0,255
# cv.imshow('Red', blank) 



# 2. draw a rectangle

# cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=cv.FILLED)
# cv.imshow('Rectangle', blank) 
                    # or
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
# cv.imshow('Rectangle', blank) 



# 3. draw a circle

# cv.circle(blank,(250,250),40,(0,0,255),thickness=-1)
# # or cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2))
# cv.imshow('Circle',blank)



#4. draw a line

# cv.line(blank,(100,100),(300,250),(255,255,255),thickness=3)
# # or in place of (250,250) --> (blank.shape[1]//2,blank.shape[0]//2))
# cv.imshow('Line',blank)



# 5. write text on img

cv.putText(blank,'Hello, my name is Swati!',(0,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)

cv.waitKey(0)