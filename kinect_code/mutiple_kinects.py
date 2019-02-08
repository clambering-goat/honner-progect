#!/usr/bin/env python
"""This goes through each kinect on your system, grabs one frame and
displays it.  Uncomment the commented line to shut down after each frame
if your system can't handle it (will get very low FPS but it should work).
This will keep trying indeces until it finds one that doesn't work, then it
starts from 0.
"""
<<<<<<< HEAD
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
=======


import freenect
import cv2
import frame_convert2

cv2.namedWindow('Depth')
cv2.namedWindow('Video')
ind = 0
print('%s\nPress ESC to stop' % __doc__)


def get_depth(ind):
    return frame_convert2.pretty_depth_cv(freenect.sync_get_depth(ind)[0])


def get_video(ind):
    return frame_convert2.video_cv(freenect.sync_get_video(ind)[0])


while 1:
    print(ind)
    try:
        depth = get_depth(ind)
        video = get_video(ind)
    except TypeError:
        ind = 0
        continue
    ind += 1
    cv2.imshow('Depth', depth)
    cv2.imshow('Video', video)
    if cv2.waitKey(10) == 27:
        break
>>>>>>> bd71dfc6d0ad9d3b9e214a4da72f9b5d45b09cee
    #freenect.sync_stop()  # NOTE: Uncomment if your machine can't handle it
