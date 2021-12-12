import cv2
import numpy as np

def general(mask,color,frame):
	contours,_ = cv2.findContours( mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	for c in contours:
		area = cv2.contourArea(c)
		if area > 5000:
			x,y,w,h = cv2.boundingRect(c)
			cv2.rectangle(frame,(x,y),(x+w,y+h), color, 3)
			cv2.putText(frame, 'Con Tapaboca', (x+10,y+20), 1, 0.9, color, 1, cv2.LINE_AA)

def run():
	cap = cv2.VideoCapture(0)
	
	redBajo1 = np.array([71,50,62],np.uint8)#Rojo
	redAlto1 = np.array([130,255,163],np.uint8)	
	while True:
		ret,frame = cap.read()
		if ret == True:
			frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			maskRed = cv2.inRange(frameHSV, redBajo1, redAlto1)
			general(maskRed,[0,255,0],frame)

			cv2.imshow('Streaming', frame)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

	cap.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	run()
