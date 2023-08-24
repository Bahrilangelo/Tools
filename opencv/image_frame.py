import cv2

img = cv2.imread('E:\www\python\AI RPS\me.jpg')

replicate = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect_101 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP)
greenColor = [0, 255, 0]
constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=greenColor)

cv2.imshow('main', img)
cv2.imshow('replicate', replicate)
cv2.imshow('reflect', reflect)
cv2.imshow('reflect_101', reflect_101)
cv2.imshow('wrap', wrap)
cv2.imshow('constant', constant)

cv2.waitKey(0)
cv2.destroyAllWindows()