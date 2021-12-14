import cv2
import numpy as np

def general(mask,color,frame):

	#Nos devuelve el contorno del tapabocas
	contours,_ = cv2.findContours( mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	for c in contours:
		#Buscamos el area del contorno
		area = cv2.contourArea(c)
		#Filtramos el ruido por areas
		if area > 3000:
			#creamos unas dimenciones para que el usuario visualice cuando tiene tapabocas y cuando no
			x,y,w,h = cv2.boundingRect(c)
			#Diferenciamos si el tapabocas esta mal colocado o bien colocado por su altura
			#Mostramos en la imagen los datos de clasificacion
			if h > 200 or w > 200:
				pass#No corresponde a tamaño de un tapabpcas
			elif h > 70:
				cv2.rectangle(frame,(x,y),(x+w,y+h), color, 3)
				cv2.putText(frame, f'Con Tapaboca', (x+10,y+20), 1, 0.9, color, 1, cv2.LINE_AA)
			else:
				cv2.rectangle(frame,(x,y),(x+w,y+h), [0,0,255], 3)
				cv2.putText(frame, f'Tapaboca mal colocado', (x+10,y+20), 1, 0.9, [0,0,255], 1, cv2.LINE_AA)



def run():
	#Se establece la captura de imagenes. 
	#En este caso activamos la camara de computador
	cap = cv2.VideoCapture(0)
	
	#Hacemos la busqueda que corresponda con el color del tapabocas
	#Mediante una seleccion de color HSV
	redBajo1 = np.array([87,90,47],np.uint8)#Rojo
	redAlto1 = np.array([122,255,245],np.uint8)	

	#Ciclo de trabajo
	while True:

		#Lectura de imagen en cada trame y corroboramos la camara este activa
		ret,frame = cap.read()
		if ret == True:
			#Convertimos el sistema de defecto BGR a HSV
			frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			#Buscamos el rango de colores de la imagen
			mask = cv2.inRange(frameHSV, redBajo1, redAlto1)
			#Llamado a la funcion
			general(mask,[0,255,0],frame)
			#Mostramos la imagen
			cv2.imshow('Streaming', frame)
			#control de escape
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
			#Guarda imagenes del momento
			elif cv2.waitKey(1) & 0xFF == ord('c'):
				cv2.imwrite('CapturDetection.png',frame)
				cv2.imwrite('CapturHSV.png',mask)

	#Cerramos todo adecuadamente
	cap.release()
	cv2.destroyAllWindows()

#Funcionamiento del programa
if __name__ == "__main__":
	run()
