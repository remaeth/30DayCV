import cv2
#hehhehehe
#read webcam
webcam = cv2.VideoCapture(0)

#visualize webcam
while True:
    ret, frame = webcam.read()

    cv2.imshow('frame', frame)
    #stops when user clicks the letter 'q'
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

#release memory allocated
webcam.release()
cv2.destroyAllWindows()