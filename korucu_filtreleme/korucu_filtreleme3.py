import cv2
import numpy as np


kamera=cv2.VideoCapture(0)


while(1):

    ret, frame=kamera.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    dk = np.array([100,60,60])
    uk = np.array([140,255,255])


    laplacian=cv2.Laplacian(frame,cv2.CV_64F)
    sobelX=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobelY=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    mask=cv2.inRange(hsv,dk,uk)
    son=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('orjinal hali',frame)
    cv2.imshow('lap',laplacian)
    cv2.imshow('sx', laplacian)
    cv2.imshow('sy', laplacian)
    cv2.imshow('son',son)
    if cv2.waitKey(25) & 0XFF==ord('q'):
        break


kamera.release()
cv2.destroyAllWindows()