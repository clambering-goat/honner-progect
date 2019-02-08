#!/usr/bin/env python
"""This goes through each kinect on your system, grabs one frame and
displays it.  Uncomment the commented line to shut down after each frame
if your system can't handle it (will get very low FPS but it should work).
This will keep trying indeces until it finds one that doesn't work, then it
starts from 0.
"""
import freenect
import cv2 as cv
import frame_convert


ind = 1
print('%s\nPress ESC to stop' % __doc__)


while 1:
    print(ind)
    try:
	(freenect.sync_get_depth(0)[0])
	print("got file 1")
    except TypeError:

	print("faile to get data from 1 ")
    freenect.sync_stop()
    try:
	(freenect.sync_get_depth(1)[0])
	print("got file 2")
    except TypeError:

	print("faile to get data from 2 ")
    freenect.sync_stop()
    #freenect.sync_stop()  # NOTE: Uncomment if your machine can't handle it
