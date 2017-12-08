#!/usr/bin/python2

import cv2,time

data=cv2.VideoCapture(0)

#  starting web cam

status,frame=data.read()
#  camera started or not 
print(status)
# frame is current focus image by camera

cv2.imshow('windowname',frame)
cv2.waitKey(0)
cv2.destroyAllWindows()


