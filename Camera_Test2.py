import time
import picamera
import numpy as np
import cv2 as cv

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 90 
    time.sleep(0.1)
    image = np.empty((480, 640, 3), dtype=np.uint8)
    #times the operation of taking and converting a picture
    start = time.time()
    camera.capture(image, 'bgr',use_video_port = True)

    #done = time.time()
#converts the image in grayscale for quicker computation
img = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

#end = time.time()
#print(end-start)

#detect solid  shapes

ret, thresh = cv.threshold(img, 31,255, 0)
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(start-time.time())

#cv.drawContours(img, contours, -1, (0,255,0), 3)

#trying something
img = cv.bilateralFilter(img, 5, 45,95 )
img = cv.blur(img,(5,5))


v = np.median(img)
sigma = 0.33

#---- apply optimal Canny edge detection using the computed median----
lower_thresh = int(max(0, (1.0 - sigma) * v))
upper_thresh = int(min(255, (1.0 + sigma) * v))

#detect outlines
edges = cv.Canny(img,lower_thresh,upper_thresh, apertureSize = 3)

print(time.time()-start)

cv.imshow("window title", edges)

cv.waitKey(0)

