import cv2

vid = cv2.VideoCapture(0)
# PC kamerasi disinda kamera varsa 0 yerine indexleri yazilir

while True:
    ret, frame = vid.read()

    cv2.imshow('frame', frame)

    #kInp = cv2.waitKey(0)
    # bu sifir bekleme suresi
    kInp = cv2.waitKey(1)

    if kInp == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()