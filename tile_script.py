from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import imutils
# from imutils.video import VideoStream
import numpy as np
import time

import serial
class Connection():
    def __init__(self, path, frequency):
        self.serial = serial.Serial(path, frequency, timeout=1)
        self.serial.flush()
        print ("HERE")
    def sendTap(self, number):
        # if number != 1:
        #     return
        assert (number in range(1,5))
        self.serial.write(str.encode(str(number) + '\n'))
    def sendTaps(self, numbers):
        # if number != 1:
        #     return
        assert (len(numbers) == 4)
        print ("".join(map(str, numbers)))
        self.serial.write(str.encode("".join(map(str, numbers)) + '\n'))
    
    def read(self):
        # line = self.serial.readline().decode('utf-8').rstrip()
        return ""

# vs = cv2.VideoCapture("test_vid.MP4")
camera = PiCamera()
shape = (400, 500)
FRAME_RATE = 85
camera.resolution = shape
camera.framerate = FRAME_RATE
raw = PiRGBArray(camera, size=shape)

conn = Connection('/dev/ttyACM0', 115200)

paused= True
current_time = lambda: int(round(time.time() * 1000))
cooldowns = [0,0,0,0]
last_time = current_time()
for frame in camera.capture_continuous(raw, format="bgr",use_video_port=True):
    frame = frame.array
    actual = frame
    frame = imutils.resize(frame, width=500)
    (H, W) = frame.shape[:2]
    #frame = frame[H//10:4*H//5 - H//5, :]
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # frame = cv2.GaussianBlur(frame, (9,9), 0)
    (thresh, frame) = cv2.threshold(frame, 50, 255, cv2.THRESH_BINARY)
    # print (frame, frame.shape)
    i = 0
    taps = [0,0,0,0]
    elapsed_time = current_time() - last_time
    last_time = current_time()
    didTap = False
    for x in range(W//8, W, W//4):
        cooldowns[i] = max(0, cooldowns[i] - elapsed_time)
        if (cooldowns[i] == 0):
            # isTap = True
            # for y in range(35):
            #     if (frame[-100 + y][x] != 0):
            #         isTap = False
            #         break
            if (frame[-100][x] == 0):
                taps[i] = 1
                cooldowns[i] = 200
                didTap = True
        i += 1
    if didTap and not paused:
        conn.sendTaps(taps)
    cv2.imshow("Frame", frame)
    # cv2.imshow("Actual", actual)
    

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break 
    elif key == ord("p"):
        paused = not paused
    raw.truncate(0)
    
# vs.release()
cv2.destroyAllWindows()
