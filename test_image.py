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
picture()
