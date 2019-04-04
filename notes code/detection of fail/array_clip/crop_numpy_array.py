

import numpy as np
import cv2
import os


def select_array(image):
    image = data.astype(np.uint8)
    r = cv2.selectROI(image)
    return(r)


run=True
for q in os.listdir("D:/numpy_data"):

    if q[-4:len(q)]==".npy":
        print(q)
        data=np.load("D:/numpy_data/"+q)

        if run ==True:
            run=False
            r=select_array(data)




        # Crop image
        data = data[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
        np.save("F:/croped_numpy/"+q,data)
        #image = data.astype(np.uint8)
        #cv2.imshow("Image", image)
        #cv2.waitKey(0)
