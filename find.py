import cv2
import math

file_path = "1.jpg"
img = cv2.imread(file_path)

pointList = []


def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 2, (0, 0, 255), 2, cv2.FILLED)
        size = len(pointList)
        if size != 0 and size % 3 != 0:
            cv2.line(img, tuple(pointList[round((size-1)/3)*3]), (x, y), (0, 0, 255), 2)
        pointList.append([x, y])


def getGradient(ptr1, ptr2):
    x1, y1 = ptr1[0], ptr1[1]
    x2, y2 = ptr2[0], ptr2[1]
    return (y2 - y1) / (x2 - x1)


def findAngle(pointList):
    ptr1, ptr2, ptr3 = pointList[-3:]
    m1 = getGradient(ptr1, ptr2)
    m2 = getGradient(ptr1, ptr3)
    angleR = math.atan((m2 - m1)/(1 + (m2*m1)))
    angleD = round(math.degrees(angleR))
    angle = abs(angleD)
    cv2.putText(img, str(angle), (ptr1[0] + 80, ptr1[1] - 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)
    print(angle)


while True:
    img = cv2.resize(img, (1280, 720))

    cv2.setMouseCallback("Image", mousePoints)
    if len(pointList) % 3 == 0 and len(pointList) != 0:
        findAngle(pointList)
    cv2.putText(img, "Press 'q' for clean the canvas .......", (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        pointList = []
        img = cv2.imread(file_path)

    if key == 27:
        break

