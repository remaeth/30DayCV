import os

import cv2

video_path = os.path.join('.', 'data', 'seal.mp4')

#read video
video = cv2.VideoCapture(video_path)

#visualize video
ret = True
while(ret):
    ret, frame = video.read()

    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(40)

#releases memory allocated
video.release()
cv2.destroyAllWindows()