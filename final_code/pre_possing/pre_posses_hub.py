import g_code_to_point_cloud
import point_could_to_x_min_max
import y_change_over_x
import numpy as np
from math import radians,sin,cos
import os





def roation(point_cloud_file,angle,rotation_axies):
    point_could_data=[]
    file=open(point_cloud_file,"r")
    point_could_data=file.readlines()
    file.close()



    angle=radians(angle)
    s = sin(angle)
    c = cos(angle)
    count=-1
    max_Z=0
    min_z=9999999999
    for l1 in point_could_data:
        points = l1.split(" ")
        x,y,z=points
        z=float(z)
        if max_Z<z:
            max_Z=z
        if min_z>z:
            min_z=z
    z_mid=min_z+((max_Z-min_z)/2)
    v1=len(point_could_data)


    rotated_point_cold=np.zeros((v1,3))
    for l1 in point_could_data:

        points=l1.split(" ")
        x,y,z=points
        count+=1

        x=float(x)-105
        y=float(y)-105
        z=float(z)-z_mid



        if rotation_axies == "x":
            x1=x
            y1=(y*c)-(z*s)
            z1=(y*s)+(z*c)

        if rotation_axies == "y":
            x1=(x*c)+(z*s)
            y1=y
            z1=(z*c)-(x*s)


        if rotation_axies == "z":
            x1=(x*c)-(y*s)
            y1=(x*s)+(y*c)
            z1=z

        x1=float(x1)+105
        y1=float(y1)+105
        z1=float(z1)+z_mid



        rotated_point_cold[count]=((x1,y1,z1))



    name = point_cloud_file
    file=open(name,"w")
    for q in rotated_point_cold:
        data=str(q[0])+" "+str(q[1])+" "+str(q[2])+"\n"
        file.write(data)

    file.close()





teast_mode=False

#step 1 -file_seletion


if teast_mode==False:
    while 1:
        user_input=input("please enter the  dir of the data")
        if os.path.isdir(user_input)==True:
            break
        else:
            print("invaild dir ")
else:
    user_input="./"


list_of_files=[]
for files in os.listdir(user_input):
    if files[-6:len(files)] == ".gcode":

        list_of_files.append(files)


file_to_open=""

if len(list_of_files)==0:
    print("no files found ")
    exit()

elif len(list_of_files) ==1:
    file_to_open=list_of_files[0]



elif len(list_of_files)>1:
    print("files found :")
    count=0
    for q in list_of_files:
        count+=1
        print(count,q)

    while 1:
        user_input=input("please enter the  number of the file you want to open")


        try:
            user_input=int(user_input)
            file_selected= user_input - 1
            file_to_open = list_of_files[file_selected]
            break

        except:
            print("invaild input ")
#
# x_roation=0
# while True:
#     try:
#         x_roation=float(input("roation object in the x axies "))
#         break
#     except:
#         print("invaild input")
#
# y_roation=0
# while True:
#     try:
#         y_roation=float(input("roation object in the y axies "))
#         break
#     except:
#         print("invaild input")

z_roation=0
while True:
    try:
        z_roation=float(input("roation object in the z axies "))
        break
    except:
        print("invaild input")


print("start g code to point cloude convert on: ",file_to_open)


step_1=g_code_to_point_cloud.g_code_to_point_cloud(file_to_open)
file_name_of_point_could=step_1.get_file_name()
print("point could make and saved to file ",file_name_of_point_could)



# if x_roation!=0:
#     print("roationing x axies")
#     roation(file_name_of_point_could,x_roation,"x")
#
# if y_roation!=0:
#     print("roation y axies ")
#     roation(file_name_of_point_could,y_roation,"y")

if z_roation!=0:
    print("roation in z axies ")
    roation(file_name_of_point_could,z_roation,"z")

print("finding max and min x points ")
step_2=point_could_to_x_min_max.get_x_min_to_x_max(file_name_of_point_could)
max_min_x=step_2.get_file_name()
print("max and min x point found saved to file ",max_min_x)


print("get only point visible to sensore ")

step_3=y_change_over_x.get_points(file_name_of_point_could)
print("file saved as ",step_3)

