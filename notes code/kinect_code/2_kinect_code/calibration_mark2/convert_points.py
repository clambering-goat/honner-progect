

import numpy as np

from math import radians,sin,cos

file_working_with="calibration_depth1"


file=open(file_working_with,"r")

file_data=file.readlines()



for q in range(len(file_data)-1):
    file_data[q]=file_data[q].strip()




for q in file_data:
    info =q.split(" ")

    if info[0]=="y rotation":
        y_rotation=info[1]

    if info[0]=="horzonatl_scan_min_point":
        horzonatl_scan_min_point=int(info[1]),int(info[2])

    if info[0]=="horzontal_scan_max_point":
        horzontal_scan_max_point=int(info[1]),int(info[2])

    if info[0]=="vertiacl_scan_min_point":
        vertiacl_scan_min_point=int(info[1]),int(info[2])

    if info[0]=="vertiacl_scan_max_point":
        vertiacl_scan_max_point=int(info[1]),int(info[2])



print(vertiacl_scan_min_point)

print(vertiacl_scan_max_point)


mid_x=(horzontal_scan_max_point[1]-horzonatl_scan_min_point[1])/2
mid_x=mid_x+horzonatl_scan_min_point[1]

mid_y=(vertiacl_scan_max_point[0]-vertiacl_scan_min_point[0])/2
mid_y=mid_y+vertiacl_scan_min_point[0]
print("mid_x",mid_x)
print("mid_y",mid_y)






name=file_working_with.split("_")
name=name[1]+".npy"
point_could_data_raw=np.load(name)



point_could_data_not_cented=[]

y_count=-1
for l1 in point_could_data_raw:
    x_count = -1
    y_count+=1
    for l2 in l1:
        x_count +=1
        x=x_count
        y=y_count
        z=l2
        point_could_data_not_cented.append((x,y,z))






#cent so the cent of  the point cous is 0,0


# useing x_mid point  320
# # using y_mid point  240
point_could_data=[]

for l1 in point_could_data_not_cented:

    x,y,z=l1
    x=x-mid_x
    y=y-mid_y
    z=255-z
    point_could_data.append((x,y,z))





roated_point_cloud=[]

angle = 180
angle = radians(angle)
print("angle",angle)
s = sin(angle)
c = cos(angle)

print("sin vaule is ",s)
for q in point_could_data:
    x,y,z=q


#box is not cent so 180 rotatrion results in misapment

    #rotation around the z axies
    #x1=(x*c)-(y*s)
    #y1=(x*s)+(y*c)
    #z1=z

    #rotation in x
    # x1=x
    # y1=(z*s)+(y*c)
    # z1=(z*c)-(y*s)

    #rotation in y
    # x1=(z*s)+(x*c)
    # y1=y
    # z1=(z*c)-(x*s)


    #rotation in y
    z1=(x*s)+(z*c)
    y1=y
    x1=(x*c)-(z*s)

    roated_point_cloud.append((x1,y1,z1))



file=open("rotaion.xyz","vaules")
for q in roated_point_cloud:
    data=str(q[0])+" "+str(q[1])+" "+str(q[2])+"\n"
    file.write(data)



for q in point_could_data:
    data=str(q[0])+" "+str(q[1])+" "+str(q[2])+"\n"
    file.write(data)

file.close()






