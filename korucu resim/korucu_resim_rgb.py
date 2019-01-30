import cv2
import numpy as np
#split,merge  metodu performans açısından kötü olduğundan kullanmamaya çalışalım

img=cv2.imread('ozel.jpg')

img[:,:,2]=220




cv2.imshow('ozelharekat',img)
cv2.waitKey()
cv2.destroyAllWindows()
