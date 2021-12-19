import cv2
import numpy as np

def count(image, contour):
	for (i, c) in enumerate(contour):
		M = cv2.moments(c)
		if( M["m00"] == 0): M["m00"] = 1
		x = int( M["m10"]/M["m00"])
		y = int( M["m01"]/M["m00"])
		cv2.putText(image, str(i+1), (x,y), 1, 1, (0,0,0), 1, cv2.LINE_AA)

img = cv2.imread("src/randomColorCircle.png")
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

yellowDown = np.array([40,255,255], np.uint8)
yellowUp = np.array([0,50,0], np.uint8)

redDown = np.array([180,255,255], np.uint8)
redUp = np.array([140,50,0], np.uint8)

blueDown = np.array([130,255,255], np.uint8)
blueUp = np.array([60,50,0], np.uint8)

yellowMask = cv2.inRange(imgHSV, yellowUp, yellowDown)
redMask = cv2.inRange(imgHSV, redUp, redDown)
blueMask = cv2.inRange(imgHSV, blueUp, blueDown)


yellowContour = cv2.findContours(yellowMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
redContour = cv2.findContours(redMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
blueContour = cv2.findContours(blueMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

cv2.drawContours(img, yellowContour, -1, (0,255,255), 2)
cv2.drawContours(img, redContour, -1, (0,0,255), 2)
cv2.drawContours(img, blueContour, -1, (255,0,0), 2)
count(img, yellowContour)
count(img, blueContour)
count(img, redContour)

cv2.imshow('circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()