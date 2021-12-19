import cv2
import numpy as np

img = cv2.imread('src/money.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 210,255, cv2.THRESH_BINARY_INV)



newImg, contornos= cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img,newImg,-1,(0,255,0),3)


i=0
for c in newImg:
	M = cv2.moments(c)
	if (M["m00"] == 0): M["m00"] = 1
	x = int( M["m10"]/M["m00"] )
	y = int( M["m01"]/M["m00"] )
	cv2.putText( 	img,
					str(i),
					(x,y),
					1,
					1.5,
					(0,0,0),
					1,
					cv2.LINE_AA)
	cv2.drawContours(img,[c],0,(0,255,0),3)
	cv2.imshow('img', img)
	cv2.waitKey(0)
	i +=1

cv2.destroyAllWindows()
