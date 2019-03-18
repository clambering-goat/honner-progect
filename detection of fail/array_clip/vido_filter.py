
import numpy as np
import os
import cv2

#home="G:/python_data/base_line/"
home="F:/croped_numpy/"


for q in os.listdir(home):

    if q[-4:len(q)]==".npy" and q[0]=="d":

        data=np.load(file_to_load)
        img = data.astype(np.uint8)
        blur = cv2.bilateralFilter(img,9,75,75)
        cv2.imshow("frame",image)
        cv2.waitKey(5)
