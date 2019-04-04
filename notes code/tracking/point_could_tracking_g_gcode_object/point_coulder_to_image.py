

import numpy as np
import cv2
file= open("point_cloud.txt","r")


data=file.readlines()

file.close()


array=[]
for q in data:
    temp=q.split(" ")
    x=float(temp[0])
    y=float(temp[1])
    z=float(temp[2])
    if z>0.2:

        array.append((x,y,z))



slioet_min_x=0
slioet_min_y=0

for w in array:
    x,y,z=w


    if x<slioet_min_x:
        slioet_min_x=x

    if y<slioet_min_y:
        slioet_min_y=y



array_noramlesd=[]

x_size=0
y_size=0

for vaules in array:
    x,y,z=vaules

    x= x - slioet_min_x
    y= y - slioet_min_y

    array_noramlesd.append((x,y,z))

    if x>x_size:
        x_size=x

    if y>y_size:
        y_size=y


x_size=round(x_size)+1
y_size=round(y_size)+1
print("x_size",x_size)
print("y_size",y_size)
data = np.zeros((y_size, x_size, 3), dtype=np.uint8)

for vaules in array_noramlesd:
    x,y,z=vaules
    x=int(x)
    y=int(y)
    z=int(z)
    data[y][x]=[z,z,z]

cv2.imshow("frame",data)
cv2.waitKey()


