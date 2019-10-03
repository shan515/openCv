import cv2
import numpy as np 
import matplotlib

img = cv2.VideoCapture(0)

while (True):
    _ , frame = img.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    lower_range = np.array([30,150,50])
    upper_range = np.array([255,255,180])
    mask = cv2.inRange(image , lower_range, upper_range)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Original", frame)
    cv2.imshow("Red", res)
    cv2.imshow("Gray", gray)
    cv2.waitKey(5)

cv2.destroyAllWindows()




