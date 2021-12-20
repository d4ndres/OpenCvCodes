import cv2 
import numpy as np


def nothing(x):
	pass

def controlBarPerTime( img, nameImg ):
	r = cv2.getTrackbarPos('L',nameImg)
	g = cv2.getTrackbarPos('S',nameImg)
	b = cv2.getTrackbarPos('H',nameImg)
	switch = '0 : OFF \n1 : ON'
	s = cv2.getTrackbarPos(switch,nameImg)
	if s == 0:
		#img[:] = 0#Funcion no implementada
		return 0
	else:

		#img[:] = [b,g,r]#Funcion no implementada	
		return [b,g,r]


def controlBar( nameDisplay ):
	cv2.namedWindow(nameDisplay)
	cv2.createTrackbar('L', nameDisplay, 0, 255, nothing)
	cv2.createTrackbar('S', nameDisplay, 0, 255, nothing)
	cv2.createTrackbar('H', nameDisplay, 0, 180, nothing)
	switch = '0 : OFF \n1 : ON'
	cv2.createTrackbar(switch, nameDisplay,0,1,nothing)


def run():

	cap = cv2.VideoCapture(0)

	control1 = np.zeros((1,500,3), np.uint8)#objetivo no implementada
	nameControl1 = 'LOW'
	controlBar(nameControl1)



	control2 = np.zeros((1,500,3), np.uint8)#Objetivo no implementado
	nameControl2 = 'HIGH'
	controlBar(nameControl2)


	ret,frame = cap.read()
	while True:



		#cv2.imshow(nameControl1, control1)#Funcion no implementada
		aux = controlBarPerTime(control1,nameControl1)		
		colorBajo1 = np.array(aux,np.uint8)

		#cv2.imshow(nameControl2, control2)#Funcion no implementada
		aux = controlBarPerTime(control2,nameControl2)		
		colorAlto1 = np.array(aux,np.uint8)



		ret,frame = cap.read()
		if ret == True:
			frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			maskRed1 = cv2.inRange(frameHSV, colorBajo1, colorAlto1)

			maskRedRGB = cv2.bitwise_and(frame, frame, mask=maskRed1) 
			#cv2.imshow('Streaming', frame)
			cv2.imshow('Rojos', maskRedRGB)

		k = cv2.waitKey(1) & 0xFF
		if k == 27: #esc
			break

	cap.release()
	cv2.destroyAllWindows()




if __name__ == '__main__':
	run()

