import cv2
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.HandDetector(detectionCon=0.8)

while True:
    _, img = cap.read()
    img = cv2.flip(img, 2)
    hands, img = detector.findHands(img, flipType=False)

    cv2.imshow("JAK Gesture Zoom Prog", img)
    cv2.waitKey(1)
