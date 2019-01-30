import cv2
import numpy as np

img=cv2.imread('ozel.jpg') #0 gri ton filtre

# print(str(img.item(200,250,2)))
#print(str(img.shape)) # yükseklik genişlk ve kanal saysı rgb
#print(str(img.size)) #pixel sayısı
#print(img.dtype) # tipini öğrenmek için
yusuf= img[130:180,350:520]
img[130:180,250:420]=yusuf
cv2.imwrite('bayrak.jpg',img)
cv2.imshow('bayrak',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
