

import numpy as np
from math import tan

import matplotlib.pyplot as plt
#1 get the x size from the g code using the siolget code gicve layer by layer



#2 find the egdes of the model

#ask for bonder box (asuuing only the modle in the box )

#find the max x







#3 using the z data conver pixel vailes in cm

#get depth_vaule usuing

#depth_vaule_in_meters(vaule)=1/(-0.0030711016*vaule+3.3309495161)


data=np.load("depth_carmea('192.168.1.240', 35920)_4.npy")

vaule=data[275][384]
print(vaule)
#
k1 = 1.1863
k2 = 2842.5
k3 = 0.1236


depth_vaule_in_meters=k3*tan(vaule/k2 + k1)
# draw=[]
# x_line=[]
# for vaule in range(2047):
#     depth_vaule_in_meters = 100 / ((-0.0030711016 * vaule) + 3.33)
#     print(depth_vaule_in_meters)
#     draw.append(depth_vaule_in_meters)
#     x_line.append(vaule)
#
# plt.plot(x_line,draw, 'ro')
# plt.axis([0, 2060, 0, 1000])
# plt.show()


#


print(depth_vaule_in_meters)
#using formla:
# 1.7*depth_vaule_in_meters*number_of_pixels



#4 compaer the 2
