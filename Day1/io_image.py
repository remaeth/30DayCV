import os

import cv2

image_path = os.path.join('.', 'data', 'bird.jpg')

#read image
img = cv2.imread(image_path)

#write image
cv2.imwrite(os.path.join('.', 'data', 'bird_out.jpg'), img)

#visualize image 
cv2.imshow('img', img)
cv2.waitKey(0)