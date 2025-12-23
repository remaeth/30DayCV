import os

import cv2
import numpy as np

img = cv2.imread(os.path.join('.', 'data', 'bird.jpg'))

#use canny edge detector for edge detection (other types: sobel and laplace operators)
img_edge = cv2.Canny(img, 250, 200)

#dilate (or thicken) lines
img_edge_dilate = cv2.dilate(img_edge, np.ones((3, 3), dtype=np.int8))

#erode (or thins) lines
img_edge_erode = cv2.erode(img_edge_dilate, np.ones((3, 3), dtype=np.int8))

cv2.imshow('img', img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_dilate', img_edge_dilate)
cv2.imshow('img_edge_erode', img_edge_erode)



cv2.waitKey(0)