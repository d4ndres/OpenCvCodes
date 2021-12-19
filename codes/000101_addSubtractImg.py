import cv2

img1 = cv2.imread('src/guaca.jpg',0)
img2 = cv2.imread('src/perfect.jpg',0)

size = img1.shape

img2 = cv2.resize(img2, size[::-1], interpolation = cv2.INTER_AREA)

result = cv2.add(img1, img2)
weigth = cv2.addWeighted(img1,0.5,img2,0.5,0)
subtract = cv2.subtract(img1,img2)
subtractABS = cv2.absdiff(img1,img2)

cv2.imshow('result', result)
cv2.imshow('weigth', weigth)
cv2.imshow('subtract', subtract)
cv2.imshow('subtractABS', subtractABS)
#cv2.imshow('a', img1)
#cv2.imshow('b', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
