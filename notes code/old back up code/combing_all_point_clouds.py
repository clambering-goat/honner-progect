import numpy as np
from math import sin cos

data1=np.load("file1.npy")
data2=np.load("file2.npy")
data3=np.load("file3.npy")


main_data=[data1,data2,data3]
file=open("kinect_point_cloud.xyz","vaules")

max_depth_vaule=255

angel=0
for data in main_data:
    angel=angel+60
    x_p=-1
    y_p=-1
    for y in data:
        y_p+=1
        x_p=-1
        for z_data in y:
            x_p+=1
            transpotion=255-z_data
            data=str(x_p)+" "+str(y_p)+" "+str(transpotion)+" \n"
            file.write(data)

file.close()
