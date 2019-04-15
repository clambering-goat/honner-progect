


import numpy as np
import random
import cv2

file_to_use="data.npy"
data=np.load(file_to_use)

depth_groups_coulers={}

max_vaule=np.amax(data)
min_vaule=np.amin(data)

x_size=len(data[0])
y_size=len(data)

couler_array=np.zeros((y_size,x_size,3),dtype=np.uint8)
print("max and min found ",max_vaule,min_vaule)


y=-1


for y_vaules in data:
    y+=1
    x=-1
    for vaules in y_vaules:
        x+=1


        if not vaules in depth_groups_coulers.keys():
            depth_groups_coulers[vaules]=random.randint(0,255),random.randint(0,255),random.randint(0,255)

        couler_array[y][x]=depth_groups_coulers[vaules]

cv2.imshow("frame",couler_array)
cv2.waitKey(0)

cv2.destroyAllWindows()

