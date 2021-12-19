import cv2

img1 = cv2.imread('guaca.jpg',0)
img2 = cv2.imread('perfect.jpg',0)
result = cv2.add(img1, img2)


cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
