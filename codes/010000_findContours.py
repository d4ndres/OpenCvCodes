import cv2
import numpy as np

'''
cv2.findContours(	imagen: imagen, 
					algoritmode recuperacion: cv2.RETR_LIST ' cv2.RETR_EXTERNAL ' cv2.RETR_CCOMP ' cv2.RETR_TREE,
					metodo; cv2.CHAIN_APPROX_NONE ' cv2.CHAIN_APPROX_SIMPLE,
					offset: desplazamiento opcional)

La funcion retorna
imgen, contornos detectados
'''

img = cv2.imread('src/ludicolo.png')
size =  np.array(img.shape[1::-1])//2
img = cv2.resize(img, size, interpolation = cv2.INTER_AREA)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,binary = cv2.threshold(gray,125,255,cv2.THRESH_BINARY)

newImg, contornos= cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,newImg,-1,(0,255,0),3)
print(newImg[0])
cv2.imshow('bin', img)

cv2.waitKey(0)
cv2.destroyAllWindows()