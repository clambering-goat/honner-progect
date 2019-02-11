

import numpy as np
import cv2
import os
#the object edge  is about 15cm from center


image_data=[]
depth_data=[]
print("files found ")
for q in os.listdir("./"):

    if q[-4:len(q)]==".npy":
        data=np.load(q)
        print(q)
        if q[0]=="c":
            image_data.append(data)
        if q[0]=="d":
            depth_data.append(data)


sensor_1=image_data[0],depth_data[0]
sensor_2=image_data[1],depth_data[1]



image_size=640,480
except_change_in_depth=5

# get the data from the dethp image from sensor_1
sensor_1_depth=sensor_1[1]

sensor_1_mid_point=sensor_1_depth[image_data[0]/2][image_size[1]/2]

print("sensor_1 mid point vaule is ",sensor_1_mid_point)


#horizontila sacn
start_point=image_size[0]/2
constant_scan=image_size[1]/2
last_scan_vaule=0


for scan_vaule in range(200):

    point_to_look_at=start_point+scan_vaule
    vaule_from_scan=sensor_1_depth[point_to_look_at][constant_scan]
    if vaule_from_scan>sensor_1_mid_point+
