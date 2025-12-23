import os

import cv2
#common use case - segmentation

img = cv2.imread(os.path.join('.', 'data', 'bird.jpg'))

#convert to binary image (or other type)
#1 - convert img to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#second param is the "global threshold" - number at which everything below goes to 0 and above goes to 255 (specified by 3rd)
ret, thres = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('img', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('thres', thres)

cv2.waitKey(0)