import numpy as np

from math import radians,sin,cos
import os


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
        self.distance_to_object_from_sensor=self.distance_to_object_from_sensor-255
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
        self.point_could_data_2 = []

        #puts 0,0 in cent of object
        for l1 in point_could_data_not_cented:
            x, y, z = l1
            #x = x - self.mid_x
            #y = y - self.mid_y
            z=z-255
            z=z-self.distance_to_object_from_sensor
            z=z-20
            self.point_could_data_2.append((x,y,z))
            z =  z*-1
            self.point_could_data.append((x, y, z))



    def data_out(self):
        return(self.point_could_data,self.point_could_data_2)


temp=converter(file_working_with="calibration_depth1")

data=temp.data_out()

temp2=converter(file_working_with="calibration_depth2")

data2=temp2.data_out()

new_data=data[0],data2[1]


file=open("rotaion.xyz","vaules")
for vaule_to_render in new_data:
    for q in vaule_to_render:
        data=str(q[0])+" "+str(q[1])+" "+str(q[2])+"\n"
        file.write(data)

#numpy to array

