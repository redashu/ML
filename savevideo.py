#!/usr/bin/python3

import  cv2
# using first camera
data=cv2.VideoCapture(0)
# defining  codec with FourCC -- its a 4-byte code XVID is the video codec for all os 
fourcc=cv2.VideoWriter_fourcc(*'XVID')
#            outputfile,video-fourcc , fps , frame size
output=cv2.VideoWriter('sample.avi',fourcc,20.0,(640,480))

while data.isOpened():
	status,frame=data.read()
	cv2.imshow('frame1',frame)
	output.write(frame)
	if cv2.waitKey(1) &  0xFF == ord('q') :
		break


data.release()
output.release()
cv2.destroyAllWindows()

