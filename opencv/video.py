import cv2

cap = cv2.VideoCapture('E:\www\python\AI RPS\haram.mp4')

if cap.isOpened() == False:
    print('Dosyaya erisilemedi')

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow('Frame', frame)

        kInp = cv2.waitKey(24)
        if kInp == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()