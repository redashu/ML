#!/usr/bin/python3

import cv2
import  numpy as np

# starting camera
data=cv2.VideoCapture(0)

while data.isOpened():
	status,frame=data.read()
	gray_data=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('grayframe',gray_data)
	if cv2.waitKey(1) & 0xFF == ord('q') :
		break
	
data.release()
cv2.destroyAllWindows()

