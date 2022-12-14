import numpy as np
import cv2 as cv
import torch
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
i = 1;
while i < 5:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    results = model(gray)
    results.show()
    if cv.waitKey(1) == ord('q'):
        break
    i+=1
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()