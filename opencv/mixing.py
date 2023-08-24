import cv2

img1 = cv2.imread('E:\www\python\AI RPS\me.jpg')
img2 = cv2.imread('E:\www\python\AI RPS\me.jpg', 0)

# Normal Toplama
totalImg = cv2.add(img1,img2)

# Aritmatik Toplama
totalImg = cv2.addWeighted(img1,0.5, img2,0.5, 0)
