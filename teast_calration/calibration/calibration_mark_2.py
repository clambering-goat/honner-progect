import numpy as np
import cv2
import os
from  math import tan ,degrees,radians,sin,cos



class kinect_claibration():
    def __init__(self,file_to_use):


        if type(file_to_use)!=type("random_string"):
            raise Exception("class need to be give a string")

        #laod the nmpy file into the code
        self.file_name=file_to_use
        self.file_data=np.load(file_to_use)


        self.sacn_range=300

        print("file loaded ",file_to_use,"\n")

        self.x_axies_size=len(self.file_data[0])
        self.y_axies_size=len(self.file_data)


        print("size of the x_axies is ",self.x_axies_size)
        print("size of the y_axies is ", self.y_axies_size)
        print(" ")

        self.size_of_error_to_acept=5
        print("size_of_error_to_acept",self.size_of_error_to_acept)
        print(" ")


        self.x_mid_point=int(self.x_axies_size/2)
        self.y_mid_point= int(self.y_axies_size/2)


        print("useing x_mid point ",self.x_mid_point )
        print("using y_mid point ", self.y_mid_point)
        print(" ")






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

            for loop_vaule in range(self.sacn_range):

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

            for loop_vaule in range(self.sacn_range):

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


            for scan_vaule in range(self.sacn_range):


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


            for scan_vaule in range(self.sacn_range):


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
        print("")



    def grafic_display_of_bonds(self):
        image_of_point_slection = np.copy(self.file_data)

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



                vaule_from_line=self.file_data[self.vertiacl_scan_min_point[1]][l1]

                list_of_points.append(vaule_from_line)
                filer_axies.append(l1)

            A = np.vstack([filer_axies, np.ones(len(filer_axies))]).T

            m, c = np.linalg.lstsq(A, list_of_points, rcond=None)[0]


            max_vaule_found=max(list_of_points)
            min_vaule_found=min(list_of_points)
            return(m,c,min_vaule_found,max_vaule_found)


        gradint_on_y,y_displament,y_min_vaule_found,y_max_vaule_found=y_rotation()

        gradint_on_x, x_displament, x_min_vaule_found, x_max_vaule_found=x_rotation()

        convert=tan(gradint_on_y)
        convert=degrees(convert)

        self.y_rotation=convert
        self.y_c_displcment=y_displament

        convert = tan(gradint_on_x)
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



    def save_config(self):
        print("saving data")
        name=self.file_name.split(".")
        name=name[0]
        file=open("calibration_"+name,"w")
        print("fiel name is ","calibration_" +name)
        data="y rotation "+str(self.y_rotation)+"\n"
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
        file.close()

temp=kinect_claibration("depth1.npy")
#temp.point_selection()
temp.point_selection()
temp.scan_around_point()

temp.grafic_display_of_bonds()
temp.calulat_rotation()
temp.save_config()