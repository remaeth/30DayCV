import os

import cv2

img = cv2.imread(os.path.join('.', 'data', 'whiteboard.jpg'))

print(img.shape)

#line         start pnt   end pnt    color (bgr), thickness
cv2.line(img, (150, 50), (350, 300), (255, 0, 0), 3)

#rectangle         top-left    bot-right   color (bgr)  thickness (negative fills-in)
cv2.rectangle(img, (400, 50), (500, 300), (0, 0, 255), 5)

#circle         center   radius  color(bgr) thickness
cv2.circle(img, (115, 175), 50, (0, 255, 0), 10)

#text            text           top-left   font                      size   color(bgr)    thickness
cv2.putText(img, "Hello World", (65, 275), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 255), 2)


cv2.imshow('img', img)
cv2.waitKey(0)