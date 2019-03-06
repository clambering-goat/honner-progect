


import numpy as np
import os
import cv2

#home="G:/python_data/base_line/"
home="G:/python_data/scaning_a_failed_print/"


# for q in os.listdir(home):
#
#     if q[-4:len(q)]==".npy" and q[0]=="d":
#         print(q)
#         file_to_load=home+q
#         image=np.load(file_to_load)
#         name="_image.png"
#         #image=(image,cv2.COLOR_GRAY2RGB)
#         image = image.astype(np.uint8)
#         cv2.imshow("frame",image)
#         cv2.waitKey(5)
#         #cv2.imwrite(name,image)
#         #exit()
#

data=np.load(home+"depth35529.npy")
data = data.astype(np.uint8)
#data=np.load(home+"couler35529.npy")
cv2.imshow("frame",data[200:-200])
cv2.waitKey(5000)

