import cv2
import numpy as np


kamera=cv2.VideoCapture(0)


while(1):

    ret, frame=kamera.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    dk = np.array([100,60,60])
    uk = np.array([140,255,255])


    mask=cv2.inRange(hsv,dk,uk)
    son=cv2.bitwise_and(frame,frame,mask=mask)
    kernel=np.ones((15,15),np.float32)/255
    smoothead=cv2.filter2D(son,-1,kernel)
    cv2.imshow('orjinal hali',frame)
    cv2.imshow('sm',smoothead)
    cv2.imshow('son',son)
    if cv2.waitKey(25) & 0XFF==ord('q'):
        break


kamera.release()
cv2.destroyAllWindows()