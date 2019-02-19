
import freenect
import numpy
import time
import cv2
mdev = freenect.open_device(freenect.init(), 0)
freenect.set_depth_mode(mdev, freenect.RESOLUTION_MEDIUM, freenect.DEPTH_REGISTERED)


count=0



def get_depth(dev,depth,time_stamp):
    array=depth
    global count
    #numpy.save(str(count),array)
    count+=1
    #time.sleep(60)
    #print(len(array),len(array[0]))
    array = array.astype(np.uint8)
    cv2.imshow('Depth image',depth)
freenect.runloop(dev=mdev,depth=get_depth)
