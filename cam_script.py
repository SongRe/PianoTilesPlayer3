#IMPORTS
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

#CONSTANTS
SHAPE = (300, 500)
FRAME_RATE = 85
#SETUP
camera = PiCamera()
camera.resolution = SHAPE
camera.framerate = FRAME_RATE
raw = PiRGBArray(camera, size=SHAPE)

#IMPLEMENTATION
time.sleep(0.1)

for frame in camera.capture_continuous(raw, format="bgr", use_video_port=True):
	image = frame.array
	cv2.imshow("Video Stream", image)
	key = cv2.waitKey(1) & 0xFF
	raw.truncate(0)
	if key == ord("q"):
		break
