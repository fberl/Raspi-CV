import numpy as np
import cv2 as cv

# piCamera
capPi = cv.VideoCapture()
# usbCamera
capUSB = cv.VideoCapture(1)

# set height
capPi.set(3, 640)
capUSB.set(3,640)
# set width
capPi.set(4, 480)
capUSB.set(4,480)
# set fps
capPi.set(5, 30)
capUSB.set(5, 30)
# set codec, use $v4l2-ctl  -d /dev/video0 --list-formats
capPi.set(6,cv.VideoWriter_fourcc('2','4','B','G'))
capUSB.set(0, cv.VideoWriter_fourcc('2','4','B','G'))


while(True):
    # capture frame by frame
    retPi, framePi = capPi.read()
    retUSB, frameUSB = capUSB.read()

    #OPERATIONS ON THE FRAME    
    grayPi = cv.cvtColor(framePi, cv.COLOR_BGR2GRAY)
    grayUSB = cv.cvtColor(frameUSB, cv.COLOR_BGR2GRAY)    
    
    # make into one image
    gray = cv.hconcat([grayPi, grayUSB])
    
    # detect edges in both images
    edgePi = cv.Canny(grayPi, 30,200)
    edgeUSB = cv.Canny(grayUSB, 30,200)
    edges = cv.hconcat([edgePi,edgeUSB])
    # display the resulting frame
    cv.imshow('frame',cv.vconcat([ gray, edges]))
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# release capture when done
capPi.release()
capUSB.release()
cv.destroyAllWindows()
 
