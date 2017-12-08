#!/usr/bin/python3
import numpy as np
#import matplotlib.pyplot as plt
import cv2
import time

# frame is current focus image by camera
#  imread() --have two functions  
#  image name and filter
# filters or image flags
#  i) cv2.IMREAD_COLOR   as numerica 1  # ignore all transparency 
#  ii) cv2.IMREAD_GRAYSCALE  as numerica 0  # load as 3 colors
#  iii)  cv2.IMREAD_UNCHANGED  as numeric -1 #  load image as including alpha channel 
"""
OPencv Does BGR during color order
"""
#data=cv2.imread('dog.jpg',1)
data1=cv2.imread('dog.jpg',0)
#   data have all numerical data 

#cv2.imshow('windowname',data)
cv2.imshow('windowname',data1)
cv2.waitKey(0)
cv2.destroyAllWindows()


