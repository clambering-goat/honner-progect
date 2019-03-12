


import  numpy as np
import cv2



data=np.load("data.npy")
iamge = data.astype(np.uint8)



for Ycount,y in enumerate(iamge):
    for x_count,x in enumerate(y):
        if iamge[Ycount][x_count]==255:
            iamge[Ycount][x_count] =0





cv2.imshow("frame",iamge)




cv2.waitKey(20000)

