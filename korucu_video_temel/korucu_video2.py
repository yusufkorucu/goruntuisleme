import cv2

kamera=cv2.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()
    griton=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Goruntu",goruntu)
    cv2.imshow("giriton",griton)

    if cv2.waitKey(25) & 0XFF==ord('s'):
        break
kamera.release()
cv2.destroyAllWindows()