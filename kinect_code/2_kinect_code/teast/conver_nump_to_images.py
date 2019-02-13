



import numpy as np
import cv2
import os


print("files found ")
for q in os.listdir("./"):

    if q[-4:len(q)]==".npy":
        print(q)
        image=np.load(q)
        print(type(image))
        name=q[:-4]+"_image.png"
        #image=(image,cv2.COLOR_GRAY2RGB)
        print(type(image))
        #image = image.astype(np.uint8)
        cv2.imwrite(name,image)
