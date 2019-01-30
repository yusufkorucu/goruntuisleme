import  cv2
import numpy as np

r1=cv2.imread('bayrak.jpg')
r2=cv2.imread('ozel.jpg')

top=cv2.add(r1,r2)

cv2.imshow('toplam', top)
cv2.waitKey(0)
cv2.destroyAllWindows()
