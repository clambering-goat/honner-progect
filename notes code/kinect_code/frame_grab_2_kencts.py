

import freenect
import cv2
import numpy


ind = 0





while 1:

    try:
        freenect.sync_stop()
        scan_1,_=(freenect.sync_get_depth(0)[0])
        break
    except:
        pass

    try:
        freenect.sync_stop()
        scan_2,_=(freenect.sync_get_depth(1)[0])
        break
    except:
        pass
      # NOTE: Uncomment if your machine can't handle it




array = scan_1.astype(np.uint8)

array_2=scan_2.astype(np.uint8)

cv2.imshow('Depth image',array)
cv2.imshow('Depth image',array_2)
print("done ")
