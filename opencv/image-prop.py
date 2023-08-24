import cv2

img = cv2.imread('E:\www\python\AI RPS\me.jpg')
img_gray = cv2.imread('E:\www\python\AI RPS\me.jpg', 0)

# Item 
# img.item(x,y,color)

# Piksel konumunu ve belirtilen rengin ne 255 uzerinden ne kadar oldugunu dondurur
# img[100,200] Piksel konumunu belirttik renk kodunu donduruyor

print('Blue', img.item(10,10, 0))
print('Green', img.item(10,10, 1))
print('Red', img.item(10,10, 2))

# Itemset 
# Belirtilen piksel konumuundaki piksel degistirilir
# img.itemset((x,y,colour), value)

img.itemset((10,20,0), 0)

for y in range(50):
    for x in range(50):
        img.itemset((x,y,0), 0)

# Shape
# img.shape
# Resmin boyutunu gosterir

print(img.shape)

# Size
# img,size
# Resmin piksel sayisi ve rengi carpar

print(img.size)

# Datatype
# img.dtype
# Resmin tipini dondurur

print(img.dtype)

# ROI
# roi = img[y1:y2, x1:x2]
# Resimden bir parca alir

roi = img[0:100, 0:100]

# Renk Filtresi
# img[0:100, 0:100. 0] = 0
# istenilen bir rengi yok eder veya baskin hale getirir

img[0:100, 0:100, 0] = 0