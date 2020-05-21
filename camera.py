#Module for controlling the camera and its related functions
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

    # initialize camera and refernce raw camera capture
def picture():
    camera = PiCamera()
    rawcapture = PiRGBArray(camera)
    # let the camera warm up
    time.sleep(0.1)
    # grab an image
    camera.capture(rawcapture, format = "bgr")
    image = rawcapture.array
    # display the image and then exit with any key press
    cv2.imshow("Image",image)
    cv2.waitKey(0)

    # initialize the camera and grab a reference to the raw camera capture(continuous video)
def video():
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 40
    rawCapture = PiRGBArray(camera, size=(640, 480))
    # allow the camera to warmup
    time.sleep(0.1)
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array
        # show the frame
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

