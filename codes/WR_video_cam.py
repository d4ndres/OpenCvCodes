#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
#Escritura y lectura de video
import cv2


def writeVideo(namefile):
	cap = cv2.VideoCapture(0)

	# Define the codec and create VideoWriter object
	fourcc = cv2.VideoWriter_fourcc(*'XVID')#Forma en la que se guardara la informacion de un .avi
	out = cv2.VideoWriter( namefile ,fourcc, 20, (640,480))#Creaciocion de la clase VideoWrite con los parametros de contruccion

	while(cap.isOpened()):#Indica si tenemos el video abierto
	    ret, frame = cap.read()#ret es un booleano que indica si estamos grabando, frame es la imagen en un instante de timepo
	    if ret==True:
	    	#flippe frame
	        #frame = cv2.imshow(frame,0)
	        # write the flipped frame

	        out.write(frame)
	        cv2.imshow('frame',frame)
	        if cv2.waitKey(1) & 0xFF == ord('q'):
	        	#indicamos cuando dejar de grabar con la q y indicamos la arquitectura del sistema
	            break
	    else:
	        break
	cap.release()
	out.release()
	cv2.destroyAllWindows()


def readVideo(namefile):
	cap = cv2.VideoCapture(namefile)

	while(cap.isOpened()):
	    ret, frame = cap.read()

	    #Cuando se transforma una matris a una imagen esta va estar en BGR
	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	    cv2.imshow('frame',gray)
	    if cv2.waitKey(20) & 0xFF == ord('q'):
	        break

	cap.release()
	cv2.destroyAllWindows()


if __name__ == "__main__":
	writeVideo('output.avi')
	readVideo('output.avi')
