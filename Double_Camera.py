#much code taken from pyimagesearch.com

from webcamvideostream import WebcamVideoStream
import cv2 as cv

class VideoStream:
    def __init__(self, src=0, usePiCamera=False,resolution = (640,480), framerate=30):
        # check to see if PiCamera should be used
        if usePiCamera:
            #only import picamera modules if necessary
            from pivideostream import PiVideoStream

            #initialize picamera and warm up sensor
            self.stream = PiVideoStream(resolution=resolution, framerate=framerate)

        # otherwise we are using OpenCV
    else:
        self.stream = WebcamVideoStream(src=src)
    
    def start(self):
        # start threaded video stream
        return self.stream.start()

    def update(self):
        # grab next frame from stream
        self.stream.update()

    def read(self):
        # return the current frame
        return self.stream.read()

    def stop(self):
        # stop the thread and release resources
        self.stream.stop()


