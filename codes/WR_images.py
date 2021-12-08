#Lectura y escritura de imagenes
import cv2

imagen = cv2.imread('agar_2.png',0)
cv2.imshow('Imagen', imagen)
cv2.imwrite('grises.png',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()