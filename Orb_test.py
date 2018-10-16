import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# piCamera
capPi = cv.VideoCapture(0)
# usbCamera
capUSB = cv.VideoCapture(1)

# set height
capPi.set(3, 640)
capUSB.set(3,640)
# set width
capPi.set(4, 480)
capUSB.set(4,480)
# set fps
capPi.set(5, 3)
capUSB.set(5, 3)
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
    #gray = cv.hconcat([grayPi, grayUSB])
    
    # initiate detector
    orb = cv.ORB_create(nfeatures = 150)

    # find keypoints in both images
    kpPi, desPi = orb.detectAndCompute(grayPi, None)
    kpUSB, desUSB = orb.detectAndCompute(grayUSB, None)    

    # draw keypoins locaion
    #kpGrayPi = cv.drawKeypoints(grayPi, kpPi,None, flags = 0)
    #kpGrayUSB = cv.drawKeypoints(grayUSB, kpUSB,None, flags =0)    

    #BFMatcher Object
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck = True)
    matches = bf.match(desPi, desUSB)

    #sort in order of distance
    matches = sorted(matches, key=lambda x:x.distance)

    img3 = cv.drawMatches(grayPi, kpPi, grayUSB, kpUSB, matches[:10],None,flags=2)

   
    #edges = cv.hconcat([edgePi,edgeUSB])
    # display the resulting frame
    cv.imshow('frame',img3)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# release capture when done
capPi.release()
capUSB.release()
cv.destroyAllWindows()
 
