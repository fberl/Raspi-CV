from imutils.video import VideoStream
import datetime
import argparse
import imutils
import time
import cv2 as cv


ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picamera", type=int, default=-1, help="whether or not use Raspi camera")
args = vars(ap.parse_args())

#initialize video stream and warm up sensor
vs = VideoStream(usePiCamera = args["picamera"] > 0).start()
time.sleep(1.0)

# loop over frames of video stream
while True:
    # grab the frame from threaded stream and resize to max width of 480 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=480)
    
    # draw timestap on frame
    timestamp = datetime.datetime.now()
    ts = timestamp.strfttime("%A %d %B %Y %I:%M:%S%p")
    cv.putText(frame, ts, (10, frame.shape[0] - 10), cv.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    # show the frame
    cv.imshow("Frame", frame)
    key = cv.waitKey(1) & 0xFF

    # if the q key is pressed, break
    if key == ord("q"):
        break

cv.destroyAllWindows()
vs.stop()

