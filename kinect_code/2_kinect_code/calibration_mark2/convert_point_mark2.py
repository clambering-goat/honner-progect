import numpy as np

from math import radians,sin,cos
import os
from open3d import  *
file_working_with="calibration_depth1"
class converter():
    def __init__(self,idex_to_use=0,set_position_angle=0):

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

            if info[0] == "y rotation":
                self.y_rotation = info[1]

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

        for l1 in point_could_data_not_cented:
            x, y, z = l1
            x = x - self.mid_x
            y = y - self.mid_y
            z =  z-self.distance_to_object_from_sensor+distance_from_calibration_object_wall_to_center
            self.point_could_data.append((x, y, z))





    def roatation(self,angle,rotation_axies):
        angle = radians(angle)
        print("angle", angle)
        s = sin(angle)
        c = cos(angle)
        count=-1
        v1=len(self.point_could_data)

        print("vaul;e ",v1)
        corected_point_could=np.zeros((v1,3))
        for l1 in self.point_could_data:
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

            corected_point_could[count]=((x1,y1,z1))

        return(corected_point_could)
temp=converter()
#base line
vaule_1=temp.roatation(0,"x")

#x rotata
#vaule_2=temp.roatation(180,"x")

#y roat
vaule_2=temp.roatation(180,"y")



v1=len(vaule_1)+len(vaule_2)
vaule_to_render=np.zeros((v1,3))

for q in range(len(vaule_1)-1):
    vaule_to_render[q]=vaule_1[q]

for q in range(len(vaule_2)-1):
    count=q+len(vaule_1)
    vaule_to_render[count]=vaule_2[q]



#numpy to array

pcd = PointCloud()
pcd.points = Vector3dVector(vaule_to_render)


mesh_frame = create_mesh_coordinate_frame(size=50, origin=[0, 0, 0])

draw_geometries([mesh_frame,pcd])

#draw_geometries([mesh_frame])

