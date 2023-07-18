import cv2
from pyzbar.pyzbar import decode

def oku_qr_kodu(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    qr_kodlari = decode(gray)
    
    for qr_kodu in qr_kodlari:
        (x, y, w, h) = qr_kodu.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        qr_icerik = qr_kodu.data.decode("utf-8")
        cv2.putText(frame, qr_icerik, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        print("QR Kod İçeriği:", qr_icerik)
    
    cv2.imshow("QR Kod Okuyucu", frame)

kamera = cv2.VideoCapture(0)

while True:
    ret, frame = kamera.read()
    oku_qr_kodu(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
