#!/usr/bin/python3
import numpy as np
#import matplotlib.pyplot as plt
import cv2
import time

data=cv2.imread('dog.jpg',1)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(data,'Hello BLU',(100,400),font,2,(255,255,0),10,cv2.LINE_AA)
# note BGR notation
# Blue (255,0,0)
# Red (0,255,0)
# green (0,0,255)
# black (0,0,0)
# white (255,255,255)
cv2.imshow('window1',data)
cv2.waitKey(0)
cv2.destroyAllWindows()

