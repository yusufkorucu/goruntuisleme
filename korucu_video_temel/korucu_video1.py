import cv2

kamera=cv2.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()
    cv2.imshow("Goruntu",goruntu)

    if cv2.waitKey(25) & 0XFF==ord('s'):
        break
kamera.release()
cv2.destroyAllWindows()
