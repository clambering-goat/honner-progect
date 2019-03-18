
import freenect
import numpy as np
import time
import cv2

int=freenect.init()
mdev = freenect.open_device(int, 0)
freenect.set_depth_mode(mdev, freenect.RESOLUTION_MEDIUM, freenect.DEPTH_REGISTERED)


<<<<<<< HEAD
#mdev2 = freenect.open_device(freenect.init(), 1)
#freenect.set_depth_mode(mdev2, freenect.RESOLUTION_MEDIUM, freenect.DEPTH_REGISTERED)
=======
mdev2 = freenect.open_device(int, 1)
freenect.set_depth_mode(mdev2, freenect.RESOLUTION_MEDIUM, freenect.DEPTH_REGISTERED)
>>>>>>> 851f7d8a2a40870019350bc52db5afdf02b61809

count=0
count2=0


def get_depth(dev,depth,time_stamp):
    print("display iage ")
    array=depth
    global count
    numpy.save(str(count),array)
    count+=1
    time.sleep(60)
    #print(len(array),len(array[0]))
    #array = array.astype(np.uint8)
    #cv2.imshow('Depth image',array)



freenect.runloop(dev=mdev,depth=get_depth)
