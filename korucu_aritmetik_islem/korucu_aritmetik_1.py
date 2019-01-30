import cv2


img=cv2.imread('bayraktarminiiha.jpg')
cv2.imshow('miniiha',img)

print(img[80,80])
img[80,80]=[255,255,255]
bolge=img[70:100,80:220]
img[0:30,0:140]=bolge
cv2.rectangle(img,(89,69),(199,120),(0,255,225),2)
cv2.imshow('iha',bolge)
cv2.imshow('miniiha',img)
cv2.imshow('iha1',bolge)
cv2.waitKey(0)
cv2.destroyAllWindows()
