import cv2
import numpy as np


def prueba1():
	bgr = np.zeros((300,300,3), dtype=np.uint8)
	#(sizex,sizey,dimentions), unsigned int 8bits
	bgr[:,:,:] = (255,0,0)

	cv2.imshow('BGR', bgr)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


def prueba2(namefile):
	bgr = cv2.imread(namefile)
	c1 = bgr[:,:,0]#Blue [desde donde, hasta donde, y el componente dimencional bgr a extraer]
	c2 = bgr[:,:,1]#Green
	c3 = bgr[:,:,2]#Red
	cv2.imshow('BGR', np.hstack([c1,c2,c3]))

	rgb = cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)
	c1 = rgb[:,:,0]#Red
	c2 = rgb[:,:,1]#Green
	c3 = rgb[:,:,2]#Blue
	cv2.imshow('RGB', np.hstack([c1,c2,c3]))#dimension unica
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def prueba3(namefile):
	bgr = cv2.imread(namefile)
	gray = cv2.cvtColor(bgr,cv2.COLOR_BGR2GRAY)
	cv2.imshow('Grises', gray)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
	prueba3('guaca.jpg')