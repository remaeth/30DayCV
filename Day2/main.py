import cv2

from util import get_limits
from PIL import Image

webcam = cv2.VideoCapture(0)

yellow = [0, 255, 255] #in bgr

while True:
    ret, frame = webcam.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #lower/upper limits (color range)
    lowerLimit, upperLimit = get_limits(color=yellow)

    #creates a mask (or template/location) of all the pixels containing the color (within the range) we want
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    #converting from np array (opencv representation) to pillow - information same
    mask_ = Image.fromarray(mask)

    #bonding box (x1, y1, x2, y2) - None if not detected
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    #x1, y1, w, h = cv2.boundingRect(mask)
    #cv2.rectangle(frame, (x1, y1), (x1+w, y1+h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()