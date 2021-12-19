import cv2
import numpy as np 


def mirrow(img):
	size = [img.shape[0],img.shape[1]*2,img.shape[2]]
	newImg = np.zeros(size, dtype=np.uint8)
	newImg[0:img.shape[0],0:img.shape[1]] = img
	newImg[:img.shape[0],img.shape[1]:img.shape[1]*2] = cv2.flip(img, 1)
	cv2.imshow('k', newImg)

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	if ret == False: break
	#frame = cv2.flip(frame,-1)
	#frame = cv2.flip(frame,1)
	#frame = cv2.flip(frame,0)
	mirrow(frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()