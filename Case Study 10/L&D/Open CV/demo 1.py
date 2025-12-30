import cv2
import numpy as np

print(cv2.__version__)
img = np.ones((5,3,3),np.uint8)
img = cv2.add(img,20)
print(img)
print(type(img))
print(img.dtype)
print(img.shape)
cv2.imshow('img',img)
cv2.waitKey(0)

