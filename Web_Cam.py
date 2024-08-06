#open wecam using open cv2

import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("cant open web cam")



cap.release()
cv2.destryAllWindow()
