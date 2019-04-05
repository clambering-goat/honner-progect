import numpy as np

from math import radians,sin,cos
import os
from open3d import  *

class converter():
    def __init__(self,idex_to_use=0,set_position_angle=0,file_working_with="calibration_depth1"):


        self.file_looking_at = file_working_with

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

            if info[0]=="numpy_file_name_is":
                self.file_name=info[1]+" "+info[2][0:-1]


        self.mid_x = (self.horzontal_scan_max_point[1] - self.horzonatl_scan_min_point[1]) / 2
        self.mid_x =self. mid_x + self.horzonatl_scan_min_point[1]
        self.mid_x=int(self.mid_x)

        self.mid_y = (self.vertiacl_scan_max_point[0] - self.vertiacl_scan_min_point[0]) / 2
        self.mid_y = self.mid_y + self.vertiacl_scan_min_point[0]
        self.mid_y=int(self.mid_y)

        print("mid_x", self.mid_x)
        print("mid_y", self.mid_y)


        point_could_data_raw = np.load(self.file_name)

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
        angle=float(angle)
        angle = radians(angle)
        point_could_y_rotate=self.roatation(angle,"x",start_point_could)

        angle = self.x_rotation
        angle=float(angle)
        angle = radians(angle)
        angle = angle * -1
        point_could_x_rotate=self.roatation(angle,"y",point_could_y_rotate)

        self.point_could_data=point_could_x_rotate


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









dir_to_look="./"
count_frames=0

for files in os.listdir(dir_to_look):
    if files[-4:len(files)]==".txt":


        temp=converter(file_working_with=files)

        temp.fix_points()
        vaule_1=temp.point_could_data

        #vaule_1=temp.roatation(0,"y")
        name = files[0:-4]+"rotaion.xyz"
        file=open(name,"w")
        for q in vaule_1:
            data=str(q[0])+" "+str(q[1])+" "+str(q[2])+"\n"
            file.write(data)

        file.close()