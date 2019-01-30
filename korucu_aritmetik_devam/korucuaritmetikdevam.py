import  cv2
import numpy as np

res1=cv2.imread('ihabizim.jpg')
res2=cv2.imread('ihabizim.jpg')


satir,sutun,kanal= res1.shape

roi=res1[0:satir,0:sutun]

res2gray=cv2.cvtColor(res2 , cv2.COLOR_BAYER_BG2GRAY)

ret, mask=cv2.threshold(res2gray,10,220,cv2.THRESH_BINARY)

cv2.imshow('mask',mask)
cv2.waitKey(0)

cv2.destroyAllWindows()
