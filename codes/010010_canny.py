import cv2
import numpy as np



def video():	
	cap = cv2.VideoCapture(0)

	while(cap.isOpened()):
		ret, frame = cap.read()

		if ret == True:
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			bords = cv2.Canny(gray, 200,255)
			cv2.imshow('Video', bords)

			if cv2.waitKey(1) & 0xFF == ord("q"):
				break

	cv2.destroyAllWindows()

def image():
	img = cv2.imread('src/money.jpg')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	bords = cv2.Canny(gray, 255,255)

	newImg, contornos= cv2.findContours(bords, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(img,newImg,-1,(0,255,0),3)

	cv2.imshow('img', img)
	cv2.imshow('canny', bords)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
	video()
