import cv2
import numpy as np

#function for getting lower and upper limits of the color given (in BGR)
def get_limits(color):

    #opencv expects images (h,w,# of channels) -> creates 3d array of 1x1 pixel
    c = np.uint8([[color]]) #insert the bgr values which you want to convert to hsv
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit

