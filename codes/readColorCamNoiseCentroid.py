import cv2
import numpy as np



def drawContours():
	cap = cv2.VideoCapture(0)

	redBajo1 = np.array([150,200,0],np.uint8)#Rojo
	redAlto1 = np.array([190,255,255],np.uint8)

	while True:
		ret,frame = cap.read()
		if ret == True:
			frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			maskRed = cv2.inRange(frameHSV, redBajo1, redAlto1)
			contours,_ = cv2.findContours( maskRed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			cv2.drawContours(frame,contours,-1,(0,0,255),3)
			cv2.imshow('streaming', frame)
			cv2.imshow('mask', maskRed)

	cap.release()
	cv2.destroyAllWindows()



def drawContoursDellNoise():
	cap = cv2.VideoCapture(0)

	redBajo1 = np.array([150,200,0],np.uint8)#Rojo
	redAlto1 = np.array([190,255,255],np.uint8)

	while True:
		ret,frame = cap.read()
		if ret == True:
			frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			maskRed = cv2.inRange(frameHSV, redBajo1, redAlto1)
			contours,_ = cv2.findContours( maskRed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			for c in contours:
				#centroid = cv2.moments(c)
				area = cv2.contourArea(c)
				if area > 200:
					cv2.drawContours(frame, [c], 0, (0,0,255), 2)
	
			cv2.imshow('Streaming', frame)
			#cv2.imshow('Rojos', maskRed)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
	cap.release()
	cv2.destroyAllWindows()

def drawContoursDellNoiseAndCentroid():
	cap = cv2.VideoCapture(0)

	redBajo1 = np.array([150,200,0],np.uint8)#Rojo
	redAlto1 = np.array([190,255,255],np.uint8)

	while True:
		ret,frame = cap.read()
		if ret == True:
			frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			maskRed = cv2.inRange(frameHSV, redBajo1, redAlto1)
			contours,_ = cv2.findContours( maskRed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			for c in contours:
				area = cv2.contourArea(c)
				if area > 1000:
					cv2.drawContours(frame, [c], 0, (0,0,255), 2)
					M = cv2.moments(c)
					if (M["m00"] == 0): M["m00"] = 1
					x = int( M["m10"]/M["m00"] )
					y = int( M["m01"]/M["m00"] )
					cv2.circle(frame,(x,y), 7, (0,255,0),-1)
					font = cv2.FONT_HERSHEY_SIMPLEX
					cv2.putText(frame, f'{x},{y}', (x+10,y), font, 0.75, (0,255,0), 1, cv2.LINE_AA)
					nuevoContorno = cv2.convexHull(c)
					cv2.drawContours(frame, [nuevoContorno], 0, [255,0,0], 3)
	
			cv2.imshow('Streaming', frame)
			#cv2.imshow('Rojos', maskRed)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
	cap.release()
	cv2.destroyAllWindows()


def general(mask,color,frame):
	contours,_ = cv2.findContours( mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	for c in contours:
		area = cv2.contourArea(c)
		if area > 1000:
			cv2.drawContours(frame, [c], 0, (0,0,255), 2)
			M = cv2.moments(c)
			if (M["m00"] == 0): M["m00"] = 1
			x = int( M["m10"]/M["m00"] )
			y = int( M["m01"]/M["m00"] )
			cv2.circle(frame,(x,y), 7, (0,255,0),-1)
			font = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(frame, f'{x},{y}', (x+10,y), font, 0.75, (0,255,0), 1, cv2.LINE_AA)
			nuevoContorno = cv2.convexHull(c)
			cv2.drawContours(frame, [nuevoContorno], 0, color, 3)

def run():
	cap = cv2.VideoCapture(0)
	redBajo1 = np.array([150,200,0],np.uint8)#Rojo
	redAlto1 = np.array([190,255,255],np.uint8)	
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


	