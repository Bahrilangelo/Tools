import cv2

img = cv2.imread('E:\www\python\AI RPS\me.jpg')

print('Original Size ->', img.shape)

imgResized = cv2.resize(img, (150, 250))

cv2.imshow('resized', imgResized)

cv2.imshow('original', img)

cv2.waitKey(0)
cv2.destroyAllWindows()