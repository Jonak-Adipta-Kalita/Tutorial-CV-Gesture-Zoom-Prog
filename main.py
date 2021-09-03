import cv2
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.HandDetector(detectionCon=0.8)

startDist = None
scale = 0
cx, cy = 500, 500

while True:
    _, img = cap.read()
    img = cv2.flip(img, 2)
    hands, img = detector.findHands(img, flipType=False)
    img1 = cv2.imread("picture.jpg")

    if len(hands) == 2:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1["center"]
        handType1 = hand1["type"]
        fingers1 = detector.fingersUp(hand1)

        hand2 = hands[1]
        lmList2 = hand2["lmList"]
        bbox2 = hand2["bbox"]
        centerPoint2 = hand2["center"]
        handType2 = hand2["type"]
        fingers2 = detector.fingersUp(hand2)

        if startDist is None:
            length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)
            startDist = length

        length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)
        scale = int((length - startDist) // 2)

        cx, cy = info[4:]

    else:
        startDist = None

    try:
        h1, w1, _ = img1.shape
        newH, newW = ((h1+scale)//2)*2, ((w1+scale)//2)*2
        img1 = cv2.resize(img1, (newW, newH))

        img[cy-newH//2:cy+newH//2, cx-newW//2:cx+newW//2] = img1
    except Exception as e:
        print(f"Exception: {e}")

    cv2.imshow("JAK Gesture Zoom Prog", img)
    cv2.waitKey(1)
