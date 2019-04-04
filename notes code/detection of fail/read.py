

import numpy as np
import os
import cv2

#home="G:/python_data/base_line/"
home="F:/croped_numpy/"

data_arrarge=np.load(home+"depth3589.npy")

for q in os.listdir(home):

    if q[-4:len(q)]==".npy" and q[0]=="d":
        #print(q)
        file_to_load=home+q
        image=np.load(file_to_load)

        np.add(data_arrarge,image)
        #name="_image.png"

        #image=(image,cv2.COLOR_GRAY2RGB)
        #image = image.astype(np.uint8)
        #cv2.imshow("frame",image)
        #cv2.waitKey(5)
        #cv2.imwrite(name,image)
        #exit()


np.save("totoal_array",data_arrarge)
data_arrarge = data_arrarge.astype(np.uint8)
cv2.imshow("frame",data_arrarge)
cv2.waitKey(50000000)



# data=np.load(home+"depth35529.npy")
# data = data.astype(np.uint8)
# #data=np.load(home+"couler35529.npy")
# cv2.imshow("frame",data)
# cv2.waitKey(500)
