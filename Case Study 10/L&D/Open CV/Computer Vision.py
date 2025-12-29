import cv2

img = cv2.imread('lena.jpg',1)
img_1 = cv2.imread('lena.jpg',0)
cv2.imshow("lena",cv2.resize(img,(1024,650)))
cv2.imwrite("lena_resized.jpg",cv2.resize(img,(1024,650)))
cv2.waitKey(0)
print(type(img))
print(img.shape)

print(type(img_1))
print(img_1.shape)
