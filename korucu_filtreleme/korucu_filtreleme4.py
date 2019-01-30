import cv2
import numpy as np


kamera=cv2.VideoCapture(0)


while(1):

    ret, frame=kamera.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    dk = np.array([100,60,60])
    uk = np.array([140,255,255])

    kenarlar=cv2.Canny(frame,100,200)

    mask=cv2.inRange(hsv,dk,uk)
    son=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('orjinal hali',frame)

    cv2.imshow('son',kenarlar)
    if cv2.waitKey(25) & 0XFF==ord('q'):
        break


kamera.release()
cv2.destroyAllWindows