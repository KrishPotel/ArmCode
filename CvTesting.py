import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_colour = np.array([35, 50, 20])
    upper_colour = np.array([85, 255, 255])
    
    mask = cv2.inRange(hsv, lower_colour, upper_colour)

    result = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Orignal Frame", result);

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()