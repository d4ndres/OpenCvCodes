#Umbralizacion, metodo de secmentacion de imagenes. separa fondo de la imagen del objeto de interes.
#https://docs.opencv.org/3.4/d7/d1b/group__imgproc__misc.html#ggaa9e58d2860d4afa658ef70a9b1115576a0e50a338a4b711a8c48f06a6b105dd98


import cv2
import numpy as np
from random import randint
import math

m, n = 500, 600
grises = np.zeros((m,n), dtype=np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(grises, 'Umbral: T = 130', (100,70), font, 1.5,(255),2,cv2.LINE_AA )


for i in range(2):
	if not i:
		yo, yf = 100,300
	else:
		yo, yf = 300,600

	for j in range(3):
		value = randint(0,255)
		grises[yo:yf, j*200: (j+2)*200 ] = value
		cv2.putText(grises, f'{value}', (j*200+50, math.floor((yo+yf)/2) ), font, 1,(255),1,cv2.LINE_AA )


cv2.imshow('grises', grises)

_, binarizada = cv2.threshold(grises,130, 255, cv2.THRESH_BINARY)#imagen, humbral, transformacion de color si cumple con el humbral, tipo de algoritmo
cv2.imshow('BINARIZADA', binarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()