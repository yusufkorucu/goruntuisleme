import cv2
import numpy as np

resim=np.zeros((400,900,3),dtype='uint8')
cv2.rectangle(resim,(15,15),(400,225),(0,255,250),1)
cv2.imshow("siyah",resim)

cv2.line(resim,(15,15),(400,225),(0,255,250),1)
cv2.circle(resim,(200,350),25,(123,45,78),3)

cv2.putText(resim,'iha-baykar-tai-vestel',(5,300),cv2.FONT_HERSHEY_COMPLEX_SMALL,3,(255,255,25),4,cv2.LINE_4)
cv2.imshow('ciz',resim)
cv2.waitKey(0)
cv2.destroyAllWindows()