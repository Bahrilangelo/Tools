import cv2

def openCamera():
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

def record_video():
    vid = cv2.VideoCapture(0)

    w = int(vid.get(3))
    h = int(vid.get(4))

    size = (w, h)

    result = cv2.VideoWriter('record.avi', cv2.VideoWriter_fourcc(*'XVID'), 24, size)

    while True:
        ret, frame = vid.read()
        
        if ret == True:
            result.write(frame)

            cv2.imshow('frame', frame)

            kInp = cv2.waitKey(1)
            if kInp == ord('q'):
                break
        else:
            break

    vid.release()
    result.release()
    cv2.destroyAllWindows()

def openPhoto():
    img = cv2.imread('image.jpg', 1)
    # 1 = renkli, 0 = siyah beyaz

    cv2.imshow('image', img)

    kInp = cv2.waitKey(0)

    if kInp == ord('q'):
        cv2.destroyAllWindows()