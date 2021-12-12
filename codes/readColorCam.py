import cv2
import numpy as np


def readStreamingCamera():
	cap = cv2.VideoCapture(0)

	#Configuraion luz bombillo noche
	#redBajo1 = np.array([160,150,100],np.uint8)#Rojo
	#redAlto1 = np.array([188,255,255],np.uint8)#Columna de colores definida por rango

	#configuracion dia
	#Alejado de la camara buena luz
	#redBajo1 = np.array([150,200,0],np.uint8)#Rojo
	#redAlto1 = np.array([190,255,255],np.uint8)#Columna de colores definida por rango
	redBajo1 = np.array([100,0,0],np.uint8)#Rojo
	redAlto1 = np.array([130,255,255],np.uint8)#Columna de colores definida por rango

	#redBajo2 = np.array([100,150,0],np.uint8)#Cuadro de colores definido por rangos
	#redAlto2 = np.array([130,255,255],np.uint8)#Azul


	while True:
		ret,frame = cap.read()
		if ret == True:
			frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
			#maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
			#maskRed = cv2.add(maskRed1, maskRed2)#Cuadro de colores definido por rangos

			maskRedRGB = cv2.bitwise_and(frame, frame, mask=maskRed1) 
			cv2.imshow('Streaming', frame)
			cv2.imshow('Rojos', maskRedRGB)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
	cap.release()
	cv2.destroyAllWindows()



if __name__ == "__main__":



	readStreamingCamera()