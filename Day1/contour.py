import os

import cv2
#contours are all seperated objects

#want objects to be white for detection - invert binary threshold
img = cv2.imread(os.path.join('.', 'data', 'birds.jpg'))
img = cv2.resize(img, (750, 461)) #resized for easy visualization

#preform invert binary threshold
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 160, 255, cv2.THRESH_BINARY_INV)

#compute contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    #removes noise
    if cv2.contourArea(cnt) > 100:
        #draws contours on original img - DON'T FORGET (-1)
        #cv2.drawContours(img, cnt, -1, (0, 255, 0), 1)

        #bounding boxes of contours
        x1, y1, w, h = cv2.boundingRect(cnt)

        cv2.rectangle(img, (x1, y1), (x1+w, y1+h), (0, 255, 0), 2)

    #print(cv2.contourArea(cnt))


cv2.imshow('img', img)
#cv2.imshow('img_gray', img_gray) 
cv2.imshow('thres', thresh) 

cv2.waitKey(0)