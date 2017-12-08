#!/usr/bin/python3
import numpy as np
#import matplotlib.pyplot as plt
import cv2
import time

data=cv2.imread('dog.jpg',1)
# drawing a line 
#   imgdata, starting , ending , color , line width
cv2.line(data,(50,50),(200,200),(255,255,0),15 )
cv2.rectangle(data,(120,180),(400,420),(255,0,0),10)
#                          radius         width
cv2.circle(data,(100,170),100,(0,0,255,),-1)
cv2.circle(data,(20,300),30,(0,255,255,),1)

#  polygon
points=np.array([[2,4],[10,30],[70,20],[50,10]],np.int32)
#                           connect
cv2.polylines(data,[points],True,(0,255,0),4)
# note BGR notation
# Blue (255,0,0)
# Red (0,255,0)
# green (0,0,255)
# black (0,0,0)
# white (255,255,255)
cv2.imshow('window1',data)
cv2.waitKey(0)
cv2.destroyAllWindows()

