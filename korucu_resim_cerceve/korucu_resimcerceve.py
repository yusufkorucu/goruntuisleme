import cv2
import  numpy as np

kirmizi=[0,0,255]

img=cv2.imread('ihabizim.jpg')

constant=cv2.copyMakeBorder(img,10,11,10,10,cv2.BORDER_CONSTANT,value=kirmizi)
cv2.imshow('asil',img)
cv2.imshow('constant',constant)
cv2.imwrite('cerceveiha.jpg',constant)
cv2.waitKey(0)
cv2.destroyAllWindows()
