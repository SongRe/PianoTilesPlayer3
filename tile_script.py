import cv2
import imutils
from imutils.video import VideoStream
import numpy as np
import time

initBox = None

vs = cv2.VideoCapture("test_vid.MP4")

paused= False
frame = None
while True:
    if not paused:
        frame = vs.read()
        frame = frame[1]

        if frame is None:
            break

        frame = imutils.resize(frame, width=500)
        (H, W) = frame.shape[:2]
        frame = frame[H//10:4*H//5 - H//5, :]
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # frame = cv2.GaussianBlur(frame, (9,9), 0)
        (thresh, frame) = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY)
        # print (frame, frame.shape)
        # contours, hierarchy = cv2.findContours(frame.astype('uint8'), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        i = 0
        for x in range(W//8, W, W//4):
            i += 1
            if (frame[-100][x] == 0):
                print ("TAP: " + str(i))
        # for idx, contour in enumerate(contours):
            # points = [contour[0]]
            # for i in range(1,len(contour)-1):
            #     # if abs(contour[i][0][0] - contour[i+1][0][0]) > 7 or abs(contour[i][0][1] - contour[i+1][0][1]):
            #     #     points.append(contour[i])
            #     # a high value indicates the contour contains mostly white, so draw the contour (I used the boundingRect)
            #     # if mean_val[0] < 100:
            # if 3 <= len(contour) <= 4:
            #     print (tuple(contour[0][0]), tuple(contour[2][0]))
            #     cv2.rectangle(frame, tuple(contour[0][0]), tuple(contour[2][0]), (100,100,100), 10)
        # print ("________")
            # print (points)
    # cv2.imshow("Frame", frame[H//3:, :])
    cv2.imshow("Frame", frame)
    

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break 
    elif key == ord("p"):
        paused = not paused
vs.release()
cv2.destroyAllWindows()