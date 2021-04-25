import cv2

cap = cv2.VideoCapture('shia2.mp4')

tracker = cv2.TrackerMOSSE_create()
ret, img = cap.read()
bbox = cv2.selectROI("img", img, False)
tracker.init(img, bbox)


def drawbox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (0, 255, 0), 2, 1)


try:
    while True:

        success, img = cap.read()

        success, bbox = tracker.update(img)

        if success:
            drawbox(img, bbox)
        else:
            print("iz ded")

        cv2.imshow("img", img)

        if cv2.waitKey(30) == 27:
            break
except:
    print("iz ded")

cap.release()
cv2.destroyAllWindows()
