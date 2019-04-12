import numpy as np

from math import radians,sin,cos
import os
from open3d import  *

class converter():
    def __init__(self,idex_to_use=0,set_position_angle=0,file_working_with="calibration_depth1"):

        distance_from_calibration_object_wall_to_center=30
        self.list_of_files=[]
        for files in os.listdir():

            if files[0:-6]=="calibration_":
                self.list_of_files.append(files)

        if len(self.list_of_files)==0:
            raise Exception ("no files found clsoeing down")


        print("files looking at ",self.list_of_files)


        print("index look at ",idex_to_use)
        self.file_looking_at = self.list_of_files[idex_to_use]

        print("file name ", self.file_looking_at)

        self.set_position_angle=set_position_angle

        print("set_position_angle ",self.set_position_angle)

        file=open(self.file_looking_at,"r")

        self.file_data=file.readlines()
        file.close()

        for q in self.file_data:
            info = q.split(" ")

            if info[0] == "y_rotation":
                self.y_rotation = info[1]
                print("set y rotation")

            if info[0]=="y_displacment":
                self.y_displacment=info[1]
                print("set y_displacment")

            if info[0]=="x_rotation":
                self.x_rotation=info[1]
                print("set x_rotation")

            if info[0]=="x_displacment":
                self.x_displacment=info[1]
                print("set x_displacment")


            if info[0] == "horzonatl_scan_min_point":
                self.horzonatl_scan_min_point = int(info[1]), int(info[2])

            if info[0] == "horzontal_scan_max_point":
                self.horzontal_scan_max_point = int(info[1]), int(info[2])

            if info[0] == "vertiacl_scan_min_point":
                self.vertiacl_scan_min_point = int(info[1]), int(info[2])

            if info[0] == "vertiacl_scan_max_point":
                self.vertiacl_scan_max_point = int(info[1]), int(info[2])




        self.mid_x = (self.horzontal_scan_max_point[1] - self.horzonatl_scan_min_point[1]) / 2
        self.mid_x =self. mid_x + self.horzonatl_scan_min_point[1]
        self.mid_x=int(self.mid_x)

        self.mid_y = (self.vertiacl_scan_max_point[0] - self.vertiacl_scan_min_point[0]) / 2
        self.mid_y = self.mid_y + self.vertiacl_scan_min_point[0]
        self.mid_y=int(self.mid_y)

        print("mid_x", self.mid_x)
        print("mid_y", self.mid_y)

        name = file_working_with.split("_")
        name = name[1] + ".npy"
        point_could_data_raw = np.load(name)

        point_could_data_not_cented=[]

        self.distance_to_object_from_sensor=int(point_could_data_raw[self.mid_y][self.mid_x])

        print("distance_to_object_from_sensor ",self.distance_to_object_from_sensor)

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

        self.point_could_data = []

        #puts 0,0 in cent of object
        for l1 in point_could_data_not_cented:
            x, y, z = l1
            x = x - self.mid_x
            y = y - self.mid_y
            z =  z-self.distance_to_object_from_sensor
            self.point_could_data.append((x, y, z))





    def roatation(self,angle,rotation_axies,point_could="not_given"):

        if point_could=="not_given":
            point_could=self.point_could_data

        if rotation_axies !="x" and rotation_axies !="y" and rotation_axies!="z":
            raise  Exception(" novalid axies of rortation given")
        angle=float(angle)
        angle = radians(angle)
        print("angle", angle)
        s = sin(angle)
        c = cos(angle)
        count=-1
        v1=len(point_could)

        print("vaul;e ",v1)
        rotated_point_cold=np.zeros((v1,3))
        for l1 in point_could:
            x,y,z=l1
            count+=1
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

            rotated_point_cold[count]=((x1,y1,z1))

        return(rotated_point_cold)





    def fix_points(self):

        start_point_could=self.point_could_data
        angle=self.y_rotation
        point_could_y_rotate=self.roatation(angle,"y",start_point_could)

        angle = self.x_rotation
        point_could_x_rotate=self.roatation(angle,"x",point_could_y_rotate)

        self.point_could_data=point_could_y_rotate


        # point_could_y_shift=[]
        # for q in point_could_x_rotate:
        #     x,y,z=q
        #
        #     x1=x-float(self.x_displacment)
        #     y1=y-float(self.y_displacment)
        #     z1=z
        #
        #     point_could_y_shift.append((x1,y1,z1))
        #
        # self.point_could_data=point_could_y_shift












temp=converter(file_working_with="calibration_depth1")

temp.fix_points()

vaule_1=temp.roatation(0,"y")


temp2=converter(file_working_with="calibration_depth2")
temp2.fix_points()
vaule_2=temp2.roatation(0,"y")





list_of_points=[]
filer_axies=[]
for l1 in range(-20,20):
    vaule_from_line =vaule_1[240+l1]

    list_of_points.append(vaule_from_line)
    filer_axies.append(l1)

A = np.vstack([filer_axies, np.ones(len(filer_axies))]).T

m, c = np.linalg.lstsq(A, list_of_points, rcond=None)[0]

print("gradint for hozontel of scan1 is ",m)







list_of_points=[]
filer_axies=[]
for l1 in range(-20,20):
    vaule_from_line =vaule_2[240+l1]

    list_of_points.append(vaule_from_line)
    filer_axies.append(l1)

A = np.vstack([filer_axies, np.ones(len(filer_axies))]).T

m, c = np.linalg.lstsq(A, list_of_points, rcond=None)[0]

print("gradint for hozontel of scan2  is ",m)







list_of_points=[]
filer_axies=[]
for l1 in range(-20,20):
    vaule_from_line =vaule_1[240*l1]

    list_of_points.append(vaule_from_line)
    filer_axies.append(l1)

A = np.vstack([filer_axies, np.ones(len(filer_axies))]).T

m, c = np.linalg.lstsq(A, list_of_points, rcond=None)[0]

print("gradint for vertaical of scan1 is ",m)







list_of_points=[]
filer_axies=[]
for l1 in range(-20,20):
    vaule_from_line =vaule_2[240*l1]

    list_of_points.append(vaule_from_line)
    filer_axies.append(l1)

A = np.vstack([filer_axies, np.ones(len(filer_axies))]).T

m, c = np.linalg.lstsq(A, list_of_points, rcond=None)[0]

print("gradint for vertaical of scan2  is ",m)










#make a numpy array to compibe arrays  and/or be rendered
v1=len(vaule_1)+len(vaule_2)
vaule_to_render=np.zeros((v1,3))


for q in range(len(vaule_1)-1):
    x,y,z=vaule_1[q]

    x=x
    y=y
    z1=z*-1

    vaule_to_render[q]=(x,y,z1)


for q in range(len(vaule_2)-1):
    count=q+len(vaule_1)
    vaule_to_render[count]=vaule_2[q]



file=open("rotaion.xyz","vaules")
for q in vaule_to_render:
    data=str(q[0])+" "+str(q[1])+" "+str(q[2])+"\n"
    file.write(data)

#numpy to array




#
#
# pcd = PointCloud()
#
#
# pcd.points = Vector3dVector(vaule_to_render)
#
#
# mesh_frame = create_mesh_coordinate_frame(size=50, origin=[0, 0, 0])
#
# draw_geometries([mesh_frame,pcd])
#
# #draw_geometries([mesh_frame])

