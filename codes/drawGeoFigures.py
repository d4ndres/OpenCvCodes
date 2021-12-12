import cv2
import numpy as np

imagen = 255*np.ones((500,500,3), dtype=np.uint8)

x1, y1 = 250,250
x2, y2 = 400,400

cv2.line(imagen, (x1,y1), (x2,y2), (255,0,0), 4)
cv2.rectangle(imagen, (x1,y1), (x2,y2), (255,0,0), 4)
cv2.circle(imagen, (x1,y1), 150, (255,0,0), 2)#En el grosor -1 rellena la figura

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen, "Figures CV2", (10,30), 0, 1, (0,255,0), 2, cv2.LINE_AA)
cv2.putText(imagen, "Figures CV2", (10,60), 1, 1, (0,255,0), 2, cv2.LINE_AA)
cv2.putText(imagen, "Figures CV2", (10,90), 2, 1, (0,255,0), 2, cv2.LINE_AA)
cv2.putText(imagen, "Figures CV2", (10,120), 3, 1, (0,255,0), 2, cv2.LINE_AA)
cv2.putText(imagen, "Figures CV2", (10,150), 4, 1, (0,255,0), 2, cv2.LINE_AA)
cv2.putText(imagen, "Figures CV2", (10,180), 5, 1, (0,255,0), 2, cv2.LINE_AA)
cv2.putText(imagen, "Figures CV2", (10,210), 6, 1, (0,255,0), 2, cv2.LINE_AA)
cv2.putText(imagen, "Figures CV2", (10,240), 7, 1, (0,255,0), 2, cv2.LINE_AA)


cv2.imshow('imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()