#open wecam using open cv2

import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("cant open web cam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)
    c = cv2.waitKey(1)
    if c == 27:
        break

w()
