import cv2
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while True:
    _, img = cap.read()

    cv2.imshow("JAK Gesture Zoom Prog", img)
    cv2.waitKey(1)
