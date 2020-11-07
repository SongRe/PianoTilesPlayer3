import picamera

SHAPE = (300, 500)
FRAME_RATE = 85

with picamera.PiCamera() as camera:
    camera.resolution = SHAPE
    camera.framerate = FRAME_RATE

    camera.start_recording('test_vid.h264')
    camera.wait_recording(15)
    camera.stop_recording()