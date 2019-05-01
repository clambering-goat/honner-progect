import numpy as np

from math import radians,sin,cos
import os
from open3d import  *

class converter():
    def __init__(self,  set_position_angle=0, cailbaration_file="calibration_depth_carmea('192.168.1.227', 54338)_49.txt",point_cloud=""):


        self.file_looking_at = cailbaration_file

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



        self.point_could_data=[]
        file=open(point_cloud,"r")
        self.point_could_data=file.readlines()
        file.close()



    def roatation(self,angle,rotation_axies,point_could_data):



        if rotation_axies !="x" and rotation_axies !="y" and rotation_axies!="z":
            raise  Exception(" novalid axies of rortation given")



        print("angle", angle)
        angle=radians(angle)
        s = sin(angle)
        c = cos(angle)
        count=-1
        v1=len(point_could_data)

        print("vaul;e ",v1)

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

        return(rotated_point_cold)





    def fix_points(self):


        start_point_could=self.point_could_data

        angle=self.y_rotation
        angle=float(angle)

        point_could_y_rotate=self.roatation(angle,"z",start_point_could)

        angle = self.x_rotation
        angle=float(angle)

        angle = angle * -1
        point_could_x_rotate=self.roatation(angle,"y",point_could_y_rotate)

        self.point_could_data=point_could_x_rotate






dir_to_look="./"
count_frames=0

for files in os.listdir(dir_to_look):
    if files[-4:len(files)]==".txt":


        temp=converter(cailbaration_file=files,point_cloud="point_cloud_of_calibartion teast_.xyz")


        porint_data=temp.point_could_data
        vaule_1=temp.roatation(-39.4,"z",porint_data)

        name = files[0:-4]+"rotaion.xyz"
        file=open(name,"w")
        for q in vaule_1:
            data=str(q[0])+" "+str(q[1])+" "+str(q[2])+"\n"
            file.write(data)

        file.close()
        break