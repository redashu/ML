#!/usr/bin/python3
import numpy as np
#import matplotlib.pyplot as plt
import cv2
import time

data=cv2.VideoCapture(0)
#   data have all numerical data 

while data.isOpened():
	status,frame=data.read()
	cv2.imshow('frame1',frame)
	if cv2.waitKey(1) &  0xFF == ord('q') :
		break 
	
data.release()
cv2.destroyAllWindows()


