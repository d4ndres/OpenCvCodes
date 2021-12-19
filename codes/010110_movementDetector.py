import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
i = 0
while True:
	ret, frame = cap.read()
	if ret == False: break
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	if i == 20:#Se puede colocar un modulo
		bgGray = gray
	if i > 20:
		dif = cv2.subtract(bgGray, gray)
		_, binary = cv2.threshold(dif,30,255,cv2.THRESH_BINARY)
		contour, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cv2.drawContours(frame, contour, -1, (0,0,255), 2)
		
		#cv2.imshow('dif', frame)

		for c in contour:
			area = cv2.contourArea(c)
			if area > 9000:
				x,y,w,h = cv2.boundingRect(c)
				cv2.drawContours(frame, [c], 0, (0,0,255), 2)
				cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

	cv2.imshow('video', frame)

	i += 1
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()