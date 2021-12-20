import cv2
import numpy as np



blueDown1 = np.array([0,194,0], dtype=np.uint8)
blueUp1 = np.array([10,255,255], dtype=np.uint8)

blueDown2 = np.array([170,194,0], dtype=np.uint8)
blueUp2 = np.array([180,255,255], dtype=np.uint8)

cap = cv2.VideoCapture(0)

i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
	    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	    mask1 = cv2.inRange(frameHSV, blueDown1, blueUp1)
	    mask2 = cv2.inRange(frameHSV, blueDown2, blueUp2)
	    mask = cv2.add(mask1, mask2)
	    mask = cv2.medianBlur(mask, 13)

	    if i == 20:
	    	bg = frame

	    if i > 20:
		    kernel = np.ones((5,5), np.uint8)
		    mask = cv2.dilate(mask, kernel, iterations=2)
		    areaColor = cv2.bitwise_and(bg, bg,mask=mask)
		    maskInv = cv2.bitwise_not(mask)
		    sinAreaColor = cv2.bitwise_and(frame, frame, mask=maskInv)
		    result = cv2.addWeighted(areaColor,1, sinAreaColor,1 , 0)

		    cv2.imshow('frame',mask)
		    cv2.imshow('area',result)
	    
	    i += 1
	    if cv2.waitKey(20) & 0xFF == ord('q'):
	        break

cap.release()
cv2.destroyAllWindows()