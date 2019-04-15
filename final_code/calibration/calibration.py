import numpy as np
import cv2
import os
from  math import atan ,degrees


class kinect_claibration():
    def __init__(self):



        self.size_of_error_to_acept=5
        print("size_of_error_to_acept",self.size_of_error_to_acept)
        print(" ")





        self.center_point=0,0



        print("passed set up ")
        print(" ")


    def scan_around_point(self):
        x_point=self.x_point_chosen
        y_point=self.y_point_chosen
        print("scaning around point given ")
        print("using the x point to scan around",x_point)
        print("using the y point to scan around",y_point)
        print("the points vaule is ",self.file_data[y_point][x_point])
        print(" ")

        def vertial_scan():
            start_point =self.y_point_chosen
            constant_scan =  self.x_point_chosen

            last_scan_vaule = self.file_data[self.y_point_chosen][self.x_point_chosen]
            max_down = -1

            for loop_vaule in range(self.sacn_range_y):

                point_to_look_at = start_point - loop_vaule
                vaule_from_scan = self.file_data[point_to_look_at][constant_scan]

                if vaule_from_scan >=last_scan_vaule + self.size_of_error_to_acept or vaule_from_scan <= last_scan_vaule - self.size_of_error_to_acept:
                    max_down = point_to_look_at + 1

                    print("set max_down to ", max_down, "with vaule ", last_scan_vaule)
                    print("vaule of next point", vaule_from_scan)
                    print()
                    break
                last_scan_vaule = vaule_from_scan
            if max_down==-1:
                print("errot in down scan")
                exit()
            last_scan_vaule = self.file_data[self.y_point_chosen][self.x_point_chosen]

            max_up = 1

            for loop_vaule in range(self.sacn_range_y):

                point_to_look_at = start_point + loop_vaule
                vaule_from_scan = self.file_data[point_to_look_at][constant_scan]

                if vaule_from_scan >= last_scan_vaule + self.size_of_error_to_acept or vaule_from_scan <= last_scan_vaule - self.size_of_error_to_acept:
                    max_up = point_to_look_at - 1
                    print("set max_up to ", max_up, "with vaule ", last_scan_vaule)
                    print("vaule of next point", vaule_from_scan)
                    print()
                    break

                last_scan_vaule = vaule_from_scan
            if max_up==-1:
                print("error in up scan")
                exit()
            return ((max_up,constant_scan),(max_down,constant_scan))

        def hozontail_scan():


            start_point = self.x_point_chosen
            constant_scan = self.y_point_chosen
            last_scan_vaule = self.file_data[self.y_point_chosen][self.x_point_chosen]
            max_right = -1


            for scan_vaule in range(self.sacn_range_x):


                point_to_look_at = start_point + scan_vaule
                vaule_from_scan = self.file_data[constant_scan][point_to_look_at]

                if vaule_from_scan >= last_scan_vaule + self.size_of_error_to_acept or vaule_from_scan <= last_scan_vaule - self.size_of_error_to_acept:
                    max_right = point_to_look_at - 1

                    print("set max_right to ", max_right, "with vaule ", last_scan_vaule)
                    print("vaule of next point", vaule_from_scan)
                    print()
                    break
                last_scan_vaule = vaule_from_scan

            if max_right==-1:
                print("error in right scan")
                exit()


            last_scan_vaule = self.file_data[self.y_point_chosen][self.x_point_chosen]
            max_left = -1


            for scan_vaule in range(self.sacn_range_x):


                point_to_look_at = start_point - scan_vaule
                vaule_from_scan = self.file_data[constant_scan][point_to_look_at]


                if vaule_from_scan >= last_scan_vaule + self.size_of_error_to_acept or vaule_from_scan <= last_scan_vaule - self.size_of_error_to_acept:
                    max_left = point_to_look_at + 1
                    print("set max_left to ", max_left, "with vaule ", last_scan_vaule)
                    print("vaule of next point", vaule_from_scan)
                    print()
                    break

                last_scan_vaule = vaule_from_scan

            if max_left==-1:
                print("error in left sacn ")
                exit()
            return ((constant_scan,max_right),(constant_scan,max_left))


        self.vertiacl_scan_max_point, self.vertiacl_scan_min_point=vertial_scan()



        self.horzontal_scan_max_point, self.horzonatl_scan_min_point=hozontail_scan()


        print("vertiacl_scan_max_point ", self.vertiacl_scan_max_point)
        print("vertiacl_scan_min_point ", self.vertiacl_scan_min_point)

        print("horzontal_scan_max_point", self.horzontal_scan_max_point)
        print("horzonatl_scan_min_point", self.horzonatl_scan_min_point)

        center_x=self.horzonatl_scan_min_point[1]+(self.horzontal_scan_max_point[1]-self.horzonatl_scan_min_point[1])/2
        center_y=self.vertiacl_scan_min_point[0]+(self.vertiacl_scan_max_point[0]-self.vertiacl_scan_min_point[0])/2

        self.center_point=center_x,center_y
        self.center_point_distance=self.file_data[int(center_y)][int(center_x)]
        print("")



    def grafic_display_of_bonds(self):
        image_of_point_slection = np.copy(self.file_data)
        image_of_point_slection = image_of_point_slection.astype(np.uint8)
        line_coloer=(255)


        #ARRAY IN PYTHON GO Y,X cv grafics go x,y
        def swap(vaue):
            return((vaue[1],vaue[0]))

        cv2.line(image_of_point_slection, swap(self.horzonatl_scan_min_point), swap(self.horzontal_scan_max_point), line_coloer, 5)
        cv2.line(image_of_point_slection, swap(self.vertiacl_scan_min_point), swap(self.vertiacl_scan_max_point), line_coloer, 5)


        cv2.imshow('image',image_of_point_slection)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



    def calulat_rotation(self):



        def x_rotation():
            print("caulationthe x rotation ")
            if self.horzontal_scan_max_point[0] != self.horzonatl_scan_min_point[0]:
                print("error the the line looking along ")
                exit()
            list_of_points = []
            filer_axies=[]

            for l1 in range(self.horzonatl_scan_min_point[1], self.horzontal_scan_max_point[1]):



                vaule_from_line=self.file_data[self.horzonatl_scan_min_point[0]][l1]

                data=str(vaule_from_line)+"\n"

                list_of_points.append(vaule_from_line)
                filer_axies.append(l1)

            A = np.vstack([filer_axies, np.ones(len(filer_axies))]).T
            m, c = np.linalg.lstsq(A, list_of_points, rcond=None)[0]


            max_vaule_found=max(list_of_points)
            min_vaule_found=min(list_of_points)
            return(m,c,min_vaule_found,max_vaule_found)


        def y_rotation():
            print("caulating the y rotation ")
            if self.vertiacl_scan_max_point[1] != self.vertiacl_scan_min_point[1]:
                print("error the the line looking along ")
                exit()
            list_of_points = []
            filer_axies=[]

            for l1 in range(self.vertiacl_scan_min_point[0], self.vertiacl_scan_max_point[0]):



                vaule_from_line=self.file_data[l1][self.vertiacl_scan_min_point[1]]
                data=str(vaule_from_line)+"\n"

                list_of_points.append(vaule_from_line)
                filer_axies.append(l1)

            A = np.vstack([filer_axies, np.ones(len(filer_axies))]).T

            m, c = np.linalg.lstsq(A, list_of_points, rcond=None)[0]


            max_vaule_found=max(list_of_points)
            min_vaule_found=min(list_of_points)
            return(m,c,min_vaule_found,max_vaule_found)


        gradint_on_y,y_displament,y_min_vaule_found,y_max_vaule_found=y_rotation()

        gradint_on_x, x_displament, x_min_vaule_found, x_max_vaule_found=x_rotation()

        convert=atan(gradint_on_y)
        convert=degrees(convert)

        self.y_rotation=convert
        self.y_c_displcment=y_displament

        convert = atan(gradint_on_x)
        convert = degrees(convert)

        self.x_rotation = convert
        self.x_c_displamnet=x_displament


        print("x axies rotation is ")
        print(self.x_rotation)
        print("c displament ")
        print(self.x_c_displamnet)
        print("max vaule found is ", x_max_vaule_found)
        print("min vaule found on line is ",x_min_vaule_found)
        print(" ")

        print("y axies rotation is ")
        print(self.y_rotation)
        print("c displament ")
        print(self.y_c_displcment)
        print("max vaule found is ", y_max_vaule_found)
        print("min vaule found on line is ", y_min_vaule_found)
        print(" ")


    def nump_data_to_use(self,file_list):

        def pre_array(index):
            data=np.load(file_list[index])
            out_data=data.astype(np.uint8)
            return out_data

        image_of_point_slection = pre_array(0)

        index=0
        while 1:

            cv2.imshow('image', image_of_point_slection)

            k = cv2.waitKey(0)



            if k==ord("s"):
                index+=1
                if index==len(file_list):
                    index=0
                print("file ",index)
                image_of_point_slection=pre_array(index)
            if k==ord("f"):
                break

        cv2.destroyAllWindows()

        # laod the nmpy file into the code
        self.file_name = file_list[index].split("/")
        self.file_name =self.file_name[-1]
        self.file_data = np.load(file_list[index])



        print("file loaded ", file_list[index], "\n")

        self.x_axies_size = len(self.file_data[0])
        self.y_axies_size = len(self.file_data)

        print("size of the x_axies is ", self.x_axies_size)
        print("size of the y_axies is ", self.y_axies_size)
        print(" ")

        self.x_half_screen_size= int(self.x_axies_size / 2)
        self.y_half_screen_size = int(self.y_axies_size / 2)

        self.sacn_range_x = self.x_half_screen_size
        self.sacn_range_y= self.y_half_screen_size
        return ()




    def point_selection(self,point_to_use="nothing"):

        if point_to_use !="nothing":
            self.y_point_chosen,self.x_point_chosen, =point_to_use
            return()
        print("start point select")
        print("double left clik to slect point")
        print("doule right click to get the point vaule ")
        print("press ecp to clsoe the program")
        print("")


        print(" ")

        # as cv2 change the array when it draws on it
        # .copy make a copy and removes any binding between
        image_of_point_slection = np.copy(self.file_data)
        self.x_point_chosen, self.y_point_chosen = -1, -1
        self.done=False
        #has to be a aprt 2 as open cv rest vaule in the function it runs in

        def point_selection_part_2(image_of_point_slection):

            image_of_point_slection = image_of_point_slection.astype(np.uint8)





            def mosue_event_handelr(event, x, y, flags, param):
                if event == cv2.EVENT_LBUTTONDBLCLK:
                    self.done=True
                    cv2.circle(image_of_point_slection, (x, y), 5, (255, 0, 0), -1)
                    self.x_point_chosen, self.y_point_chosen = x, y

                if event== cv2.EVENT_RBUTTONDBLCLK:
                    print("vaule of the point you click on is ",image_of_point_slection[y][x])
                    print(" ")







            cv2.namedWindow('image')
            cv2.setMouseCallback("image", mosue_event_handelr)
            while 1:
                cv2.imshow('image', image_of_point_slection)

                k = cv2.waitKey(20) & 0xFF
                if k==27:
                    print("esc pressed close program")
                    exit()

                if self.done==True:
                    break

            cv2.destroyAllWindows()
            return()


        point_selection_part_2(image_of_point_slection)


        print("points picked ","x ",self.x_point_chosen,"y ",self.y_point_chosen)

        print(" ")
        return()




    def x_y_offset(self):
        x,y=self.center_point




        y_edge=self.vertiacl_scan_min_point[0]

        delta_y=y_edge-y


        y_c = y*1.64*delta_y


        self.center_to_base=y_c



    def save_config(self):
        print("saving data")
        name=self.file_name[0:-4]
        #name=name[0]
        file=open("calibration_"+name+".txt","w")
        print("fiel name is ","calibration_" +name)

        data="y_rotation "+str(self.y_rotation)+"\n"
        file.write(data)

        data="y_ydisplacment "+str(self.y_c_displcment)+"\n"
        file.write(data)

        data = "x_rotation "+ str(self.x_rotation)+"\n"
        file.write(data)

        data = "x_displacment "+ str(self.x_c_displamnet)+"\n"
        file.write(data)

        data = "horzonatl_scan_min_point " + str(self.horzonatl_scan_min_point[0])+" "+str(self.horzonatl_scan_min_point[1]) + "\n"
        file.write(data)


        data = "horzontal_scan_max_point " + str(self.horzontal_scan_max_point[0])+" "+ str(self.horzontal_scan_max_point[1]) + "\n"
        file.write(data)


        data = "vertiacl_scan_min_point " + str(self.vertiacl_scan_min_point[0])+" "+str(self.vertiacl_scan_min_point[1]) + "\n"
        file.write(data)


        data = "vertiacl_scan_max_point " + str(self.vertiacl_scan_max_point[0])+" "+str(self.vertiacl_scan_max_point[1]) + "\n"
        file.write(data)

        data="center_is "+str(self.center_point) + "\n"
        file.write(data)

        data="center_distance_is " +str(self.center_point_distance) + "\n"
        file.write(data)

        data="center_to_base " +str(self.center_to_base) + "\n"
        file.write(data)

        data="numpy_file_name_is "+str(self.file_name) + "\n"
        file.write(data)


        file.close()



dir_to_look="D:/scan_notes/teast_2/"
count_frames=0
file_list={}
for files in os.listdir(dir_to_look):
    if files[-4:len(files)]==".npy" and files[0]=="d":
        key_vaule=files.split("'")
        key_vaule=(key_vaule[1])
        file_loaction=dir_to_look+files
        if key_vaule in file_list.keys():
            file_list[key_vaule].append(file_loaction)
        else:
            file_list[key_vaule]=[]
            file_list[key_vaule].append(file_loaction)


for q in file_list:
    print(q)
    print(file_list[q])


    temp=kinect_claibration()
    temp.nump_data_to_use(file_list[q])
    temp.point_selection()
    temp.scan_around_point()
    temp.grafic_display_of_bonds()
    temp.calulat_rotation()
    temp.x_y_offset()
    temp.save_config()



