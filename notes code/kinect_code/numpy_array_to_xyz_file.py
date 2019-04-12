import numpy as np


data=np.load("./save data/scan1_buble gum.npy")



file=open("kinect_point_cloud.xyz","vaules")

max_depth_vaule=255

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
