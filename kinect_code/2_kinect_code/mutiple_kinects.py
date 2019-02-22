#!/usr/bin/env python
"""This goes through each kinect on your system, grabs one frame and
displays it.  Uncomment the commented line to shut down after each frame
if your system can't handle it (will get very low FPS but it should work).
This will keep trying indeces until it finds one that doesn't work, then it
starts from 0.
"""


import freenect
import cv2
#import frame_convert2
import numpy as np

ind = 0
print('%s\nPress ESC to stop' % __doc__)

print("device fond ",len(freenect.sync_get_depth(ind)))
def get_depth(ind):
    return (freenect.sync_get_depth(ind)[0])


def get_video(ind):
    return (freenect.sync_get_video(ind)[0])


while 1:
    if ind ==2:
        break
    print(ind)
    freenect.init()
    #freenect.start_video()
    try:

        depth = get_depth(ind)
        video = get_video(ind)

    except TypeError:
        ind = 0
        continue

    ind += 1
<<<<<<< HEAD:kinect_code/mutiple_kinects.py
    cv2.imshow('Depth', depth)
    cv2.imshow('Video', video)
    if cv2.waitKey(10) == 27:
        break
=======

    array = depth.astype(np.uint8)
    name="depth"+str(ind)
    np.save(name,array)

    array = video.astype(np.uint8)
    name="clouer_image"+str(ind)
    np.save(name,array)

>>>>>>> 5f5ef2ad4cb6ffd6deb2243717f807a805fbd4e1:kinect_code/2_kinect_code/mutiple_kinects.py
    freenect.sync_stop()  # NOTE: Uncomment if your machine can't handle it
