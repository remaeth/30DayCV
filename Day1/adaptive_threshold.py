import os

import cv2

#when one "global" threshold does not work
#computes based making many small regions and finding threshold for each region

img = cv2.imread(os.path.join('.', 'data', 'writing.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#3rd parameter can be gaussian or mean
#5th must be odd
#6th is size of region
adaptive_thres = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 20)

cv2.imshow('img', img)
cv2.imshow('adaptive_thres', adaptive_thres)

cv2.waitKey(0)