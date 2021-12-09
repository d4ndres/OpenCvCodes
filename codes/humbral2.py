
import cv2
import numpy as np


def trunc(imgPath):
	#Pasa los valores que no cumplen con el humbral al valor del humbral

	grises = cv2.imread(imgPath, 0)

	_, trunc = cv2.threshold(grises,100, 5, cv2.THRESH_TRUNC)#El tercer argumento no se tiene encuenta
	cv2.imshow('Trunc', trunc)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


def toz(imgPath):
	#el tercer parametro no se tiene encuenta.
	#Al no cumplir con el humbral especificado la informacion se convertira en cero y podemos hacer la operacion ivr
	grises = cv2.imread(imgPath, 0)
	_, toZero = cv2.threshold(grises,70, 5, cv2.THRESH_TOZERO)
	_, toOne = cv2.threshold(grises,70, 5, cv2.THRESH_TOZERO_INV)
	cv2.imshow('toZero - toOne', np.hstack([toZero, toOne]))
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def binary(imgPath):
	#Como vimos anteriormente el humbral es convertido al tercer argumento
	grises = cv2.imread(imgPath, 0)
	_, binarizada = cv2.threshold(grises,52, 255, cv2.THRESH_BINARY)
	_, binarizadaInv = cv2.threshold(grises,52, 255, cv2.THRESH_BINARY_INV)
	cv2.imshow('BIN - BININV', np.hstack([binarizada,binarizadaInv]))	
	cv2.waitKey(0)
	cv2.destroyAllWindows()



if __name__ == '__main__':
	imgPath = 'you.jpg'
	binary(imgPath)
	trunc(imgPath)
	toz(imgPath)
	