import  cv2

iha=cv2.imread('iha_111.png',0)

cv2.imshow('iha1calismasi',iha)
cv2.imwrite('ihagri.png',iha)

cv2.waitKey(0)
cv2.destroyAllWindows()