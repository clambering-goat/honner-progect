import numpy as np
from math import radians,sin,cos
import os





def roation(point_cloud_file,angle,rotation_axies):
    point_could_data=[]
    file=open(point_cloud_file,"r")
    point_could_data=file.readlines()
    file.close()


    print("point_cloud_file",point_cloud_file)
    print("angle", angle)

    angle=radians(angle)
    s = sin(angle)
    c = cos(angle)
    count=-1
    v1=len(point_could_data)


    rotated_point_cold=np.zeros((v1,3))
    for l1 in point_could_data:

        points=l1.split(" ")
        x,y,z=points
        count+=1

        x=float(x)-105
        y=float(y)-105
        z=float(z)
        if rotation_axies=="y":
            z1 = (x * s) + (z * c)
            y1 = y
            x1 = (x * c) - (z * s)

        if rotation_axies=="x":
            x1=x
            y1=(z*s)+(y*c)
            z1=(z*c)-(y*s)


        if rotation_axies == "z":
            x1=(x*c)-(y*s)
            y1=(x*s)+(y*c)
            z1=z

        x1=float(x1)+105
        y1=float(y1)+105
        z1=float(z1)

        rotated_point_cold[count]=((x1,y1,z1))



    name = point_cloud_file[0:-4]+"rotaion.xyz"
    file=open(name,"w")
    for q in vaule_1:
        data=str(q[0])+" "+str(q[1])+" "+str(q[2])+"\n"
        file.write(data)

    file.close()


point_cloud_file
angle
rotation_axies
roation(point_cloud_file,angle,rotation_axies)
