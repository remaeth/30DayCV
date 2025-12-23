import os

import cv2

#blur is good at removing noise from images

img = cv2.imread(os.path.join('.', 'data', 'bird.jpg'))

#size of the proximity/area (neighbors)
#blurring = average of k_size neighbors
#smaller k_size = less blur
k_size = 7
img_blur = cv2.blur(img, (k_size, k_size))

#gaussian blur has an additional parameter
#almost identical to normal blur but lightly different
img_gaussian_blur = cv2.GaussianBlur(img, (k_size, k_size), 3)

#always takes a square
#good at removing noise (depending on type)
img_median_blur = cv2.medianBlur(img, k_size)


cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gaussian_blur', img_gaussian_blur)
cv2.imshow('img_median_blur', img_median_blur)

cv2.waitKey(0)