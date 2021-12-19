import cv2
import numpy as np


def try1():
	img1 = np.zeros((400,600), dtype=np.uint8)
	x, y, w, h = 100, 200, 200, 200
	img1[x:x+w,y:y+h] = 255

	img2 = np.zeros((400,600), dtype=np.uint8)
	x, y, r = 300, 200, 125
	img2 = cv2.circle(img2, (x,y), r, (255), -1)

	#cv2.imshow('img1', img1)
	#cv2.imshow('img2', img2)


	_and = cv2.bitwise_and(img1,img2)
	cv2.imshow('and', _and)
	_or = cv2.bitwise_or(img1,img2)
	cv2.imshow('or', _or)
	_not = cv2.bitwise_not(img1)
	cv2.imshow('or', _not)
	_xor = cv2.bitwise_xor(img1,img2)
	cv2.imshow('xor', _xor)


	cv2.waitKey(0)
	cv2.destroyAllWindows()



def try2():
	cap = cv2.VideoCapture(0)

	circle = np.zeros((480,640), dtype=np.uint8)
	x, y, r = 300, 200, 125
	mask = cv2.circle(circle, (x,y), r, (255), -1)

	while cap.isOpened():
		ret, frame = cap.read()
		#print(frame.shape)
		if ret:
			result = cv2.bitwise_and(frame, frame, mask=mask)
			cv2.imshow('video', result)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
	cap.release()

if __name__ == "__main__":
	try2()