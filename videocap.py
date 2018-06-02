#!/usr/bin/python3

import cv2,time

cap=cv2.VideoCapture(0)

while cap.isOpened():
    #  here status return true or false 
    # frame is the actual data captured by camera
    status,frame=cap.read()
    # converting image from color to gray 
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('camera0',frame)
    cv2.imshow('camera1',gray)
    cv2.imshow('camera2',frame)
    cv2.imshow('camera3',gray)
    if cv2.waitKey(1) & 0xFF == ord('q') :
        
        break

cap.release()
cv2.destroyAllWindows()


