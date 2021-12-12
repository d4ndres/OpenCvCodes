import cv2
import numpy as np


def tryColor():
	img = cv2.imread('TablaHSV.png')
	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	#Regido por la tabla HSV
	#H el rango de colores
	#S La saturacion del color 0->claro(o blanco) 255->El color en su maxima intensidad
	#V el valor. 0 -> oscuro hasta quedar sin color. 255->Color en maximo explendor 
	requestRangeColorLow = np.array([100,0,0], np.uint8) 
	requestRangeColorHigh = np.array([140,100,255], np.uint8) 
	requestRangeColor = cv2.inRange(imgHSV, requestRangeColorLow,requestRangeColorHigh)
	colorFinded = cv2.bitwise_and(img,img,mask=requestRangeColor)

	cv2.imshow('colors', img)
	#cv2.imshow('HSV', imgHSV)
	cv2.imshow('Finded', colorFinded)
	cv2.waitKey(0)
	cv2.destroyAllWindows

def tryColor2():
	img = cv2.imread('TablaHSV.png')
	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)



	requestRangeColorLow1 = np.array([50,100,0], np.uint8) 
	requestRangeColorHigh1 = np.array([70,150,255], np.uint8)	
	requestRangeColorLow2 = np.array([160,200,45],np.uint8) 
	requestRangeColorHigh2 = np.array([180,255,255],np.uint8)


	requestRangeColor1 = cv2.inRange(imgHSV, requestRangeColorLow1,requestRangeColorHigh1)
	requestRangeColor2 = cv2.inRange(imgHSV, requestRangeColorLow2,requestRangeColorHigh2)
	requestRangeColor = cv2.add(requestRangeColor1, requestRangeColor2)#Permite colocar diferentes areas de color en una misma deteccion
	colorFinded = cv2.bitwise_and(img,img,mask=requestRangeColor)

	cv2.imshow('colors', img)
	#cv2.imshow('HSV', imgHSV)
	cv2.imshow('Finded', colorFinded)
	cv2.waitKey(0)
	cv2.destroyAllWindows	

if __name__ == "__main__":
	tryColor2()