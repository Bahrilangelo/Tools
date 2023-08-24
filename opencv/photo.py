import cv2

img = cv2.imread('E:\www\python\AI RPS\me.jpg', 0)

cv2.imshow('Profil', img)

cv2.waitKey(0)
cv2.destroyAllWindows()


img = cv2.imread('E:\www\python\AI RPS\me.jpg', 0)
cv2.imwrite('me2', img, 0)
 