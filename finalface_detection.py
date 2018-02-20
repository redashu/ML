#!/usr/bin/python3

import  cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


img=cv2.imread('banjovi.jpg')
while True:
	grayimg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(grayimg,1.15,5)  
	for  (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
		roi_gray=grayimg[y:y+h,x:x+w]
		roi_color=img[y:y+h,x:x+w]
	
	cv2.imshow('imgw',img)
	k=cv2.waitKey(30) & 0xff
	if k == 27:
		break		

cv2.destroyallWindows()

"""
cv2.imshow('gray',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
