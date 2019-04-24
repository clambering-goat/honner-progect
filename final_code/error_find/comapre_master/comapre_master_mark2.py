


#

import os
import numpy as np
import cv2

class compare:
    def __init__(self):


        self.printer_center_x=105

        self.center_point_x_image = 355
        self.center_point_y_image = 269


        self.max_distance=1020
        self.min_distance=610

        self.distance_to_base_mm=31.58

        self.max_distance_to_base_in_pixsels = self.y_mm_to_pixel(self.min_distance, self.distance_to_base_mm)
        self.min_distance_to_base_in_pixsels = self.y_mm_to_pixel(self.max_distance, self.distance_to_base_mm)

        print("max distance to print bed in pixels is ", self.max_distance_to_base_in_pixsels)
        print("min distance to print bed in pixels is ", self.min_distance_to_base_in_pixsels)

    def y_mm_to_pixel(self,distance_to_object_mm, size_in_mm):
        pixels_size = size_in_mm / (1.64 * (distance_to_object_mm / 1000))
        pixels_size = round(pixels_size)
        pixels_size = int(pixels_size)
        return pixels_size

    def y_pixel_to_mm(self,distance_to_object_mm, number_of_pixels):
        mm_size = (distance_to_object_mm / 1000) * 1.64 * number_of_pixels
        return mm_size

    def load_in_data(self,where_to_look="./"):
        numpy_file = ""
        max_point_file = ""
        y_over_x_file = ""

        for files in os.listdir(where_to_look):
            if files[0:5] == "chane":
                y_over_x_file = files
            if files[-4:len(files)] == ".npy":
                numpy_file = files
            if files[0:5] == "x_max":
                max_point_file = files
        print("load files ")
        print("nump file ", numpy_file)
        print("y_over_x file ", max_point_file)
        print("x max and min file ", y_over_x_file)


        #load in the scan daat and make couler copy of data

        self.scan_data=np.load(numpy_file)
        couler_vesion_of_scan = np.copy(self.scan_data)
        couler_vesion_of_scan = couler_vesion_of_scan.astype(np.uint8)
        self.couler_vesion_of_scan = cv2.cvtColor(couler_vesion_of_scan, cv2.COLOR_GRAY2RGB)


        #load  in the scan of the vitual model
        file = open(y_over_x_file, "r")
        file_data = file.readlines()
        file.close()

        self.z_point_from_model = []
        self.x_scan_across = {}
        for raw_data in file_data:

            x, y, z = raw_data.split(" ")
            x = float(x)
            y = float(y)
            z = float(z)

            if not z in self.x_scan_across.keys():
                self.x_scan_across[z] = []
                self.z_point_from_model.append(z)
            self.x_scan_across[z].append((x, y))




        file = open(max_point_file, "r")
        file_data = file.readlines()
        file.close()
        # line exasmeple
        # 124.8 125.2 85.2 75.2 105 125.2 1.3
        # x_max=124.8 125.2
        # x_min=85.2 75.2
        # x_center=105 125.2
        # current_hight_model=1.3

        self.model_size = {}
        for x_max_data in file_data:
            split_data = x_max_data.split(" ")

            x_max_point = float(split_data[0])
            x_min_point = float(split_data[2])
            x_mid_point = float(split_data[4])
            current_hight_model = float(split_data[6])

            self.model_size[current_hight_model] = x_max_point, x_min_point, x_mid_point

        self.draw_line((self.center_point_x_image, self.center_point_y_image), (0, 255, 0),2)
        self.display_data("center point ")



    def point_in_vaid_size_range(self,point):
        y,x=point
        margion_error=5

        distance_vaule_from_scan = self.scan_data[y][x]

        if distance_vaule_from_scan > self.min_distance-margion_error and distance_vaule_from_scan < self.max_distance+margion_error:
            return True
        else:
            return False

    def find_point_00(self):
        #does not work need fix



        def find_base():
            start_point_y=self.center_point_y_image
            start_point_x=self.center_point_x_image

            shift=0
            out_point=[0,0]
            while True:
                shift+=1
                point=start_point_y+shift,start_point_x
                if   self.point_in_vaid_size_range(point):
                    out_point=point[1],point[0]
                    break

            return out_point


        self.start_point=find_base()

        self.draw_line((self.start_point))
        self.display_data("base point")


    def compare(self,layer,y_pixel_scan_point):


        hight=self.z_point_from_model[layer]
        print("comapreing at hight of ",hight)
        max_x,min_x,x_center=self.model_size[hight]

        print("max_x,min_x",  max_x,min_x)
        picels_error_margion=5


        def meaning_changins_in_model():
            number_of_y_chanes=0
            old_vaule=self.x_scan_across[hight][0]
            for vaules in self.x_scan_across[hight][1:]:

                x1,y1=vaules
                x2,y2=old_vaule


                if abs(y1-y2)>5:
                    number_of_y_chanes+=1


                old_vaule=vaules


            return number_of_y_chanes



        def z_change_compare(p1,p2,change_in_z_from_scan):
            p1=p1-3
            p2=p2+3


            print("x scan range is ",p1,p2)


            def findclosests_point(p1):

                closenst_match=-8
                z_vaule=0
                min_distance_between_points=99999

                for points in self.x_scan_across[hight]:
                    x,z=points

                    DITANCE_BETTWEN_POINTS = abs(x - p1)
                    if DITANCE_BETTWEN_POINTS <min_distance_between_points :
                        min_distance_between_points=DITANCE_BETTWEN_POINTS
                        closenst_match=x
                        z_vaule=z

                return closenst_match,z_vaule





            model_x1,model_z1=findclosests_point(p1)
            model_x2,model_z2=findclosests_point(p2)


            print(p1," cloest points is ", model_x1)
            print("model_z1",model_z1)
            print(p2, " cloest points is ", model_x2)
            print("model_z2",model_z2)

            model_z_change=model_z2-model_z1
            print("model_z_change ",model_z_change)
            print("change_in_z_from_scan ",change_in_z_from_scan)



            if model_z_change>change_in_z_from_scan-5 and model_z_change<change_in_z_from_scan+5:
                return True
            else:
                return False





            #find close match start and end point for the points
            #make a small list of point ehter side
            #comapre the distance change if any match return true

        match = 0
        no_match = 0

        #sacn to the right
        scan_cuurent_point=self.center_point_x_image, y_pixel_scan_point,self.scan_data[y_pixel_scan_point][self.center_point_x_image]
        current_x_mm =self.printer_center_x
        under_size_r=True
        over_size_r=False
        print("SCAN RIGHT ")

        aount_of_invasild_point_to_take=5
        while True:

            if aount_of_invasild_point_to_take == 0:
                break



            shift=1

            scan_old_point=scan_cuurent_point



            z_vaule=self.scan_data[y_pixel_scan_point][scan_cuurent_point[0]+shift]

            scan_cuurent_point=scan_old_point[0]+shift,scan_cuurent_point[1],z_vaule




            #print("scan_cuurent_point",scan_cuurent_point)
            if scan_cuurent_point[2] < self.min_distance or scan_cuurent_point[2] > self.max_distance:
                print("invail depth vaule found at ", scan_cuurent_point[0:2])
                print("distance vasule ", scan_cuurent_point[2])
                aount_of_invasild_point_to_take-=1
                continue




            z1=scan_old_point[2]
            z2=scan_cuurent_point[2]
            z1=int(z1)
            z2=int(z2)


            change_in_z_from_scan=z2-z1

            if abs(change_in_z_from_scan)>5:
                distance=z1
            else:
                distance=z1+change_in_z_from_scan/2






            old_x_in_mm=current_x_mm


            current_x_mm=current_x_mm+self.y_pixel_to_mm(distance,1)




            if abs(change_in_z_from_scan)>10:
                print("meaningful change from in scan")
                print("xmm point",old_x_in_mm,current_x_mm)
                if z_change_compare(old_x_in_mm,current_x_mm,change_in_z_from_scan):
                    print("change found in model ")
                    match+=1
                else:
                    no_match+=1





            if current_x_mm > max_x - picels_error_margion and current_x_mm < max_x + picels_error_margion:
                under_size_r = False

            if current_x_mm > max_x + picels_error_margion:
                over_size_r=True

            #print(" ")
            #print(" ")
            #print(" ")


        print("max x vausle found in sacn ",current_x_mm)
        # sacn to the left
        scan_cuurent_point = self.center_point_x_image, y_pixel_scan_point, self.scan_data[y_pixel_scan_point][self.center_point_x_image]
        current_x_mm = self.printer_center_x
        under_size_l = True
        over_size_l = False
        print("SCAN LEFT ")
        aount_of_invasild_point_to_take = 5
        while True:
            if aount_of_invasild_point_to_take == 0:
                break




            shift = -1

            scan_old_point = scan_cuurent_point

            z_vaule = self.scan_data[y_pixel_scan_point][scan_cuurent_point[0] + shift]

            scan_cuurent_point = scan_old_point[0] + shift, scan_cuurent_point[1], z_vaule

            #print("scan_cuurent_point", scan_cuurent_point)
            if scan_cuurent_point[2] < self.min_distance or scan_cuurent_point[2] > self.max_distance:
                print("invail depth vaule found at ", scan_cuurent_point[0:2])
                print("distance vasule ", scan_cuurent_point[2])
                aount_of_invasild_point_to_take-=1
                continue

            z1 = scan_old_point[2]
            z2 = scan_cuurent_point[2]
            z1 = int(z1)
            z2 = int(z2)

            change_in_z_from_scan = z2 - z1

            if abs(change_in_z_from_scan) > 5:
                distance = z1
            else:
                distance = z1 + change_in_z_from_scan / 2

            old_x_in_mm = current_x_mm

            current_x_mm = current_x_mm - self.y_pixel_to_mm(distance, 1)

            if abs(change_in_z_from_scan) > 10:
                print("meaningful change from in scan")
                print("xmm point", old_x_in_mm, current_x_mm)
                if z_change_compare(old_x_in_mm, current_x_mm, change_in_z_from_scan):
                    print("change found in model ")
                    match += 1
                else:
                    no_match += 1


            if current_x_mm > min_x - picels_error_margion and current_x_mm < min_x + picels_error_margion:
                under_size_l= False

            if current_x_mm < min_x - picels_error_margion:
                over_size_l = True

        print("min x vausle found in sacn ", current_x_mm)
        number_of_y_chaing_in_models = meaning_changins_in_model()
        print("number_of_y_chaing_in_models",number_of_y_chaing_in_models)



        print("-----")
        print("results ")
        print("match ",match)
        print("no_match ",no_match)

        if number_of_y_chaing_in_models == match + no_match:
            print("number of changes match up True ")
        else:
            print("number of changes match up False ")

        print("under_size_l",under_size_l)
        print("under_size_R",under_size_r)
        print("over_size_l",over_size_l)
        print("over_size_r",over_size_r)

        return (match,no_match,number_of_y_chaing_in_models,under_size_l,under_size_r,over_size_l,over_size_r)










    def comapre_hub(self):

        def get_next_scan():
            file_to_load="./old/scan_part_2_at_angle.npy"
            self.scan_data = np.load(file_to_load)
            couler_vesion_of_scan = np.copy(self.scan_data)
            couler_vesion_of_scan = couler_vesion_of_scan.astype(np.uint8)
            self.couler_vesion_of_scan = cv2.cvtColor(couler_vesion_of_scan, cv2.COLOR_GRAY2RGB)



        def find_start_of_object():
            shift=0


            #find bottem
            y_bottem_y_point=0

            #add bit about dictuce incers
            max_number_of_bad_points=10

            while True:
                shift+=1
                point=self.start_point
                x,y=point
                y=y-shift
                x=x

                if not self.point_in_vaid_size_range((y,x)):
                    max_number_of_bad_points=max_number_of_bad_points-1

                if max_number_of_bad_points==0:

                    print("no object found ")
                    break

                if  self.point_in_vaid_size_range((y, x)):


                    y_bottem_y_point=y
                    self.draw_line((x,y_bottem_y_point))
                    self.display_data("object in  printer ")

                    break


            print("y top ",y_bottem_y_point)
                #self.compare()
            self.y_bottem_y_point=y_bottem_y_point
            return True
    
    
    
            
        y=find_start_of_object()


        get_next_scan()
        y=find_start_of_object()
        cv2.line(self.couler_vesion_of_scan, (self.center_point_x_image, self.y_bottem_y_point -5),(self.center_point_x_image + 10, self.y_bottem_y_point - 5), (255, 0, 0), 1)
        self.display_data("compare _ image point ")

        for w in range(0,420,10):
            for q in range(0,100):


                match,no_match,number_of_y_chaing_in_models,under_size_l,under_size_r,over_size_l,over_size_r=self.compare(w,self.y_bottem_y_point-q)

                if under_size_l==False  and over_size_l==False:

                    cv2.line(self.couler_vesion_of_scan, (self.center_point_x_image, self.y_bottem_y_point - q),
                             (self.center_point_x_image - 10, self.y_bottem_y_point - q), (0, 255, 0), 1)

                elif under_size_r==False and over_size_r==False:
                    cv2.line(self.couler_vesion_of_scan, (self.center_point_x_image, self.y_bottem_y_point - q),
                             (self.center_point_x_image + 10, self.y_bottem_y_point - q), (0, 255, 0), 1)


                else:
                    cv2.line(self.couler_vesion_of_scan, (self.center_point_x_image, self.y_bottem_y_point - q),
                             (self.center_point_x_image + 10, self.y_bottem_y_point - q), (0,0,255), 1)
                    cv2.line(self.couler_vesion_of_scan, (self.center_point_x_image, self.y_bottem_y_point - q),
                             (self.center_point_x_image - 10, self.y_bottem_y_point - q), (0,0,255), 1)

                if under_size_l==False  and over_size_l==False and under_size_r==False and over_size_r==False:
                    cv2.line(self.couler_vesion_of_scan, (self.center_point_x_image, self.y_bottem_y_point - q),
                             (self.center_point_x_image + 10, self.y_bottem_y_point - q), (255,0,0), 2)

                    cv2.line(self.couler_vesion_of_scan, (self.center_point_x_image, self.y_bottem_y_point - q),
                             (self.center_point_x_image - 10, self.y_bottem_y_point - q), (255, 0, 0), 1)
            self.display_data("results")

    def draw_line(self,start,couler=(0,0,255),size=1):


        cv2.line(self.couler_vesion_of_scan, start, (start[0],start[1]+10), couler, size)



    def display_data(self,name=""):
        cv2.imshow(name, self.couler_vesion_of_scan)

        cv2.waitKey(500)
        cv2.destroyAllWindows()

        couler_vesion_of_scan = np.copy(self.scan_data)
        couler_vesion_of_scan = couler_vesion_of_scan.astype(np.uint8)
        self.couler_vesion_of_scan = cv2.cvtColor(couler_vesion_of_scan, cv2.COLOR_GRAY2RGB)

temp=compare()
temp.load_in_data()

temp.find_point_00()
temp.comapre_hub()
#temp.compare(35)
