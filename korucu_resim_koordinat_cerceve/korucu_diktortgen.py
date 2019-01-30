import cv2

resim=cv2.imread("ihabizim.jpg")

cv2.imshow("iha", resim)

cv2.rectangle(resim,(200,150),(820,650),(255,0,0),2)
cv2.imshow("dortgenCerceve",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()