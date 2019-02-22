
import freenect
import numpy as np

import time



try:
    #mdev = freenect.open_device(freenect.init(), 0)
    #freenect.set_depth_mode(mdev, freenect.RESOLUTION_MEDIUM, freenect.DEPTH_REGISTERED)
    while 1:


        data=freenect.sync_get_depth()

        
        for q in data:
            print(type(q))

        print(data[1])

except Exception as e:
    print(e)
