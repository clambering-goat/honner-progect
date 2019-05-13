

import os
import numpy as np
import cv2
import time
teast_mode=False

class main_class:

    def __init__(self, dir_of_scan_data, dir_code_gcode):

        # error margions
        self.z_axies_error_margion = 2
        self.y_axies_margtion_for_error = 2


        self.start_scan_at = 5
        # loacation of where the numpy file will be saved
        self.dir_of_scan_data = dir_of_scan_data

        self.ip_to_use="192.168.1.227"
        self.aount_of_y_changes_to_misse=2
        # loaction of where the gcode transcipts will be sent
        self.gcode_tarnscrip_loaction = dir_code_gcode

        # vaule from the printer manual
        self.printer_center_x_mm = 105

        # vaule from the cailbation step
        self.center_point_x_image = 310
        self.center_point_y_image = 270
        self.distance_to_base_mm = 31.58


        self.max_distance_from_sensor = 1020
        self.min_distance_from_sensor = 610

        # setting the y range of where the models will be printed
        max_distance_to_base_in_pixsels = self.y_mm_to_pixel(
            self.min_distance_from_sensor, self.distance_to_base_mm)
        min_distance_to_base_in_pixsels = self.y_mm_to_pixel(
            self.max_distance_from_sensor, self.distance_to_base_mm)

        print(
            "max distance to print bed in pixels is ",
            max_distance_to_base_in_pixsels)
        print(
            "min distance to #print bed in pixels is ",
            min_distance_to_base_in_pixsels)

        self.y_start_point_range = self.center_point_y_image + \
            min_distance_to_base_in_pixsels, self.center_point_y_image + max_distance_to_base_in_pixsels

        print("self.ruff_base_point_range")
        print(self.y_start_point_range)

    # convert mm into pixels vaules

    def y_mm_to_pixel(self, distance_to_object_mm, size_in_mm):
        pixels_size = size_in_mm / (1.64 * (distance_to_object_mm / 1000))
        pixels_size = round(pixels_size)
        pixels_size = int(pixels_size)
        return pixels_size

    # the flow function are used to conver to scan data into mm measurments

    def y_pixel_to_mm(self, distance_to_object_mm, number_of_pixels):
        mm_size = (distance_to_object_mm / 1000) * 1.64 * number_of_pixels
        return mm_size

    def x_pixel_to_mm(self, distance_to_object_mm, number_of_pixels):
        mm_size = (distance_to_object_mm / 1000) * 1.7 * number_of_pixels
        return mm_size

    def load_in_perfect_model(self, where_to_look="./"):

        # the code will look in the give dir for the files it need
        max_point_file = ""
        y_over_x_file = ""
        for files in os.listdir(where_to_look):
            if files[0:5] == "chane":
                y_over_x_file = files

            if files[0:5] == "x_max":
                max_point_file = files

        # if the files are not found the code will exit
        if max_point_file == "":
            print("max_point_file no found EXITING CODE")
            exit()

        if y_over_x_file == "":
            print("y_over_x_file no found EXITING CODE")
            exit()

        print("max_point_file", max_point_file)
        print("y_over_x_file", y_over_x_file)

        # load the file into memory
        file = open(y_over_x_file, "r")
        file_data = file.readlines()
        file.close()

        # break dowm the prefict models into layer along the y axies
        # as well was makeing a list of all the hight vaule for all layers
        self.z_point_from_model = []
        self.x_scan_across = {}

        for raw_data in file_data:

            x, y, z = raw_data.split(" ")

            x = float(x)
            y = float(y)
            z = float(z)

            if z not in self.x_scan_across.keys():
                self.x_scan_across[z] = []
                self.z_point_from_model.append(z)

            self.x_scan_across[z].append((x, y))

        # load the file into memory
        file = open(max_point_file, "r")
        file_data = file.readlines()
        file.close()

        # splits up the data for each layer
        self.model_size = {}

        for x_max_data in file_data:

            split_data = x_max_data.split(" ")

            x_max_point = float(split_data[0])
            x_min_point = float(split_data[2])
            x_mid_point = float(split_data[4])
            current_hight_model = float(split_data[6])

            self.model_size[current_hight_model] = x_max_point, x_min_point, x_mid_point

    def data_from_file_name(self, given_string):

        raw_sting = given_string.split("_")

        raw_ip = raw_sting[1]
        raw_ip = raw_ip.split("'")
        ip = raw_ip[1]

        raw_scan_numner_time_stamp = raw_sting[-1]
        raw_scan_numner_time_stamp = raw_scan_numner_time_stamp[0:-4]
        scan_number_raw, time_stamp_raw = raw_scan_numner_time_stamp.split(" ")

        time_stamp_raw = time_stamp_raw.split(".")
        time_stamp_raw = time_stamp_raw[0]

        time_stamp = int(time_stamp_raw)
        scan_number = int(scan_number_raw)

        return scan_number, time_stamp, ip

    def find_first_scan(self):

        # each scan is give  a sequential numbing as well a the time the scan was taken
        # the code blow will look for the scan with the lowest number and load
        # into memory

        first_scan_number = 9999999
        file_name = ""

        for files in os.listdir(self.dir_of_scan_data):

            if files[-4:len(files)] == ".npy" and files[0] == "d":

                raw_data = files.split("_")
                raw_data = raw_data[-1]
                raw_data = raw_data.split(" ")

                scan_number = int(raw_data[0])

                if scan_number < first_scan_number:
                    file_name = files
                    first_scan_number = scan_number

        if file_name == "":

            print("could not find any scan data in ", self.dir_of_scan_data)
            print("closeing code ")
            exit()

        self.current_file_name = file_name
        self.load_in_numy_file(self.current_file_name)

    def load_in_numy_file(self, file_name):
        # laod the numpy file into memory and make a couler copy of it for
        # dispplay resions


        file_to_load=(self.dir_of_scan_data+file_name)

        self.scan_data = np.load(file_to_load)

        couler_vesion_of_scan = np.copy(self.scan_data)
        couler_vesion_of_scan = couler_vesion_of_scan.astype(np.uint8)
        self.couler_vesion_of_scan = cv2.cvtColor(
            couler_vesion_of_scan, cv2.COLOR_GRAY2RGB)
        self.display_data("image",10)
        print(" ")


    def is_point_in_vaild_z_range(self, point):

        x,y,z = point
        distance_vaule_from_scan = self.scan_data[y][x]

        if distance_vaule_from_scan > self.min_distance_from_sensor - \
                self.z_axies_error_margion and distance_vaule_from_scan < self.max_distance_from_sensor + self.z_axies_error_margion:
            return True
        else:
            return False

    def comare_layers(self, model_layer, scan_layer):
        # compares a live layer in the vitual model to that of a layer from the
        # scan

        def find_changes_in_z_axiex_from_perfect_models():
            # scan from the left to right of a layer in the perfict models and
            # find all z changes above the 1/2 of the  error margion

            def count_z_changes(point_list):
                if len(point_list)<2:
                    return 0
                old_vaule = point_list[0]
                number_of_y_chanes = 0
                for vaules in point_list[1:]:

                    x1, y1 = vaules
                    x2, y2 = old_vaule

                    if abs(y1 - y2) > self.z_axies_error_margion:
                        number_of_y_chanes += 1

                    old_vaule = vaules

                return number_of_y_chanes

            left_points = []
            right_points = []

            # get the x_mid_point
            for points in self.x_scan_across[model_layer]:
                x, y = points

                if x >= self.printer_center_x_mm:
                    right_points.append(points)

                if x <= self.printer_center_x_mm:
                    left_points.append(points)




            number_of_y_chanes_left = count_z_changes(left_points)
            number_of_y_chanes_right = count_z_changes(right_points)

            return (number_of_y_chanes_left, number_of_y_chanes_right)




        def z_change_compare(p1, p2, change_in_z_from_scan):
             # looks to see if a chane in the z axies form the scane occurs in
             # the same place in the prefict model_layer

            def findclosests_point(point):
                # matches the cloest point between the perfect models and the
                # scan data

                closest_match = []
                z_vaule = 0
                for points in self.x_scan_across[model_layer]:

                    x, z = points

                    DITANCE_BETTWEN_POINTS = abs(x - point)

                    if DITANCE_BETTWEN_POINTS < 10:

                       closest_match.append((x,z))


                return closest_match

            matches_1= findclosests_point(p1)

            matches_2 = findclosests_point(p2)
            if teast_mode:
                print("matches_1",matches_1)
                print("matches_2",matches_2)
            for loop1 in matches_1:
                for loop2 in matches_2:

                    model_z_change = loop1[1] - loop2[1]

                    if model_z_change > change_in_z_from_scan - \
                            self.z_axies_error_margion and model_z_change < change_in_z_from_scan + self.z_axies_error_margion:
                        return True

            return False

        def scan_across(
                picels_error_margion,
                direction,
                x_limt,
                y_pixel_scan_start_point):
            # scans out from the center point comapreing size and makeing sure any z chane is orring the the right place
            # direction is what way to move
            # +1=RIGHT
            # -1=left

            z_change_match = 0
            z_chage_no_match = 0
            scan_cuurent_point = self.center_point_x_image, y_pixel_scan_start_point, self.scan_data[
                y_pixel_scan_start_point][self.center_point_x_image]
            y_starts=scan_cuurent_point[2]
            current_x_mm = self.printer_center_x_mm
            under_size = True
            over_size = False

            while True:

                # load in the 2 point that will be evuaded
                scan_old_point = scan_cuurent_point

                z_vaule = self.scan_data[y_pixel_scan_start_point][scan_cuurent_point[0] + direction]

                scan_cuurent_point = scan_old_point[0] + direction, scan_cuurent_point[1], z_vaule

                # end the loop if a invailed depth vaild is hit
                if self.is_point_in_vaild_z_range(scan_cuurent_point)==False:
                    if current_x_mm==self.printer_center_x_mm:
                        return (True,True,True)

                    break

                # deals with numpy scaler vaule and the problem with using them
                # in maths
                z1 = scan_old_point[2]
                z2 = scan_cuurent_point[2]
                z1 = int(z1)
                z2 = int(z2)

                change_in_z_from_scan = z2 - z1

                # looks to see if the cahnge in deoth is signect
                # if is is a mid point between vaules is found so acomadate the
                # x , y mm measurements
                if abs(change_in_z_from_scan) > self.z_axies_error_margion * 2:
                    distance = z1
                else:
                    distance = z1 + change_in_z_from_scan / 2

                old_x_in_mm = current_x_mm
                if direction>0:
                    current_x_mm = current_x_mm + self.x_pixel_to_mm(distance, 1)
                if direction<0:
                    current_x_mm = current_x_mm - self.x_pixel_to_mm(distance, 1)


                if abs(change_in_z_from_scan) > self.z_axies_error_margion * 2:
                    if teast_mode:
                        cv2.line(self.couler_vesion_of_scan, (scan_cuurent_point[0], 300),
                                 (scan_cuurent_point[0], 320), (255, 0, 0), 2)
                        # print("z change found at ",current_x_mm)
                        # print("change_in_z_from_scan",change_in_z_from_scan)
                    if z_change_compare(
                            old_x_in_mm,
                            current_x_mm,
                            change_in_z_from_scan):
                        if teast_mode:
                            cv2.line(self.couler_vesion_of_scan, (scan_cuurent_point[0], 300),
                                      (scan_cuurent_point[0], 320), (0, 255, 0), 2)
                        z_change_match += 1
                       # print("macth")

                    else:
                        if teast_mode:
                            cv2.line(self.couler_vesion_of_scan, (scan_cuurent_point[0], 300),
                                      (scan_cuurent_point[0], 320), (0, 0, 255), 2)

                        z_chage_no_match += 1
                       # print("no match")
                   # print("\n\n")

                if current_x_mm > x_limt - \
                        picels_error_margion and current_x_mm < x_limt + picels_error_margion:
                    under_size = False

                if direction > 0:

                    if current_x_mm > x_limt + picels_error_margion:
                        over_size = True


                if direction < 0:
                    if current_x_mm < x_limt - picels_error_margion:
                        over_size = True

            #(number_of_y_chanes_left, number_of_y_chanes_right,angle_l,angle_r)
            if direction > 0:
                z_not_match = True
                number_of_y_chanes_right,y_change_l = find_changes_in_z_axiex_from_perfect_models()
                if teast_mode:
                    print("except y chane ",number_of_y_chanes_right)
                    print("got ")
                    print("z_change_match",z_change_match)
                    print("z_chage_no_match",z_chage_no_match)

                if z_change_match > number_of_y_chanes_right - self.aount_of_y_changes_to_misse and z_change_match < number_of_y_chanes_right + self.aount_of_y_changes_to_misse and z_chage_no_match==0:#<self.aount_of_y_changes_to_misse:
                    z_not_match = False


            if direction < 0:
                z_not_match = True
                number_of_y_chanes_left,y_change_R = find_changes_in_z_axiex_from_perfect_models()


                if teast_mode:
                    print("except y chane ",number_of_y_chanes_left)
                    print("got ")
                    print("z_change_match",z_change_match)
                    print("z_chage_no_match",z_chage_no_match)

                if z_change_match > number_of_y_chanes_left-self.aount_of_y_changes_to_misse and z_change_match < number_of_y_chanes_left+self.aount_of_y_changes_to_misse and  z_chage_no_match ==0:#<self.aount_of_y_changes_to_misse:
                    z_not_match = False



            if teast_mode:
                self.display_data("conapere results",0)

            return (under_size, over_size, False)
            #return (under_size, over_size, False)
        max_x, min_x, x_center = self.model_size[model_layer]

        # scalible error margions depenting on the size of the layer the code is looking for
        # TODO: find good vasule for scalible error or remove constaer errpr
        # margion
        if max_x - min_x > 800:
            picels_error_margion = 5
        if max_x - min_x > 40:
            picels_error_margion = 7

        elif max_x - min_x > 30:
            picels_error_margion = 8

        elif max_x - min_x > 20:
            picels_error_margion = 9

        else:
            picels_error_margion = 10

        #picels_error_margion = 12

        # sacn left



        left_scan_data = scan_across(picels_error_margion, -1, min_x,scan_layer)

        # scan RIGHT

        right_scan_data = scan_across(picels_error_margion, 1, max_x,scan_layer)

        return left_scan_data, right_scan_data


    def current_print_hight(self):

        file = open(self.gcode_tarnscrip_loaction, "r")

        data = file.readlines()
        file.close()

        hight_vaules_found = []
        for w in data:
            for q in w:

                if "DONE" in q:
                    print("printer done ")
                    print("closing code")
                    exit()

                if q == "Z":
                    time_stamp = w.split("G")
                    time_stamp = time_stamp[0]
                    time_stamp = time_stamp[1:]
                    time_stamp = time_stamp.split(".")
                    time_stamp = int(time_stamp[0])

                    layer_hight = w.split(" ")
                    layer_hight = layer_hight[-1]
                    layer_hight = layer_hight.strip()
                    layer_hight = layer_hight[1:]
                    layer_hight = float(layer_hight)

                    if layer_hight<0:
                        continue

                    # print("name", name, "time_stamp", time_stamp)
                    hight_vaules_found.append((layer_hight, time_stamp))

        if len(hight_vaules_found)<0:
            return [0]
        #print("hight_vaules_found",hight_vaules_found[-1])
        return (hight_vaules_found[-1])

    def main_compare(self):

        def get_next_scan():

            m_scan_number, m_time_stamp,_ = self.data_from_file_name(
                self.current_file_name)
            m_scan_number = m_scan_number + 1
            current_time = 0
            for files in os.listdir(self.dir_of_scan_data ):

                if files[-4:len(files)] == ".npy" and files[0] == "d":
                    scna_number, current_time,ip = self.data_from_file_name(files)
                    if self.ip_to_use==ip:
                        if scna_number == m_scan_number:
                            self.current_file_name =  files
                            break



            self.load_in_numy_file(self.current_file_name)

        def load_scan_at_set_time(give_time):

            min_scan_vaile = 9999999
            for files in os.listdir(self.dir_of_scan_data):

                if files[-4:len(files)] == ".npy" and files[0] == "d":
                    scna_number, current_time,ip = self.data_from_file_name(files)
                    if self.ip_to_use==ip:
                        if current_time > give_time and min_scan_vaile > scna_number:
                            self.current_file_name =  files
                            min_scan_vaile = scna_number

            self.load_in_numy_file(self.current_file_name)
        def find_layer_0(layer_index):


            layer_mm=self.z_point_from_model[layer_index]
            matching_points = []
            #print("layer_mm",layer_mm)

            for y_scan_points in range(self.y_start_point_range[0],self.y_start_point_range[1]):
                left_data, right_data = self.comare_layers(layer_mm, y_scan_points)
                if teast_mode:
                    print(left_data, right_data)
                    cv2.line(self.couler_vesion_of_scan, (self.center_point_x_image, y_scan_points),
                             (self.center_point_x_image + 10, y_scan_points), (255, 0, 0), 2)
                    self.display_data("comapre", 0)

                left_pass = True
                for vaule in left_data:
                    if vaule==True:
                        left_pass = False

                right_pass = True
                for vaule in right_data:
                    if  vaule==True:
                        right_pass = False


                if left_pass and right_pass:
                    matching_points.append(y_scan_points)


            if len(matching_points)==0:
                return 9999
            lowest_y_point = max(matching_points)
            if teast_mode:
                cv2.line(self.couler_vesion_of_scan, (self.center_point_x_image, y_scan_points),
                         (self.center_point_x_image + 10, y_scan_points), (255, 0, 0), 2)
                self.display_data("base", 0)

            return lowest_y_point

        def compare_models(
                y_scan_range,
                model_scan_range,
                y_scan_start_point,
                start_hight_mm,comapre_results):
            y_scan_range_start = round(y_scan_range[0])
            y_scan_range_stop = int(y_scan_range[1])

            model_scan_range_start = model_scan_range[0]
            model_scan_range_stop = model_scan_range[1]




            for model_index in range(
                    model_scan_range_start,
                    model_scan_range_stop):
                model_layer = self.z_point_from_model[model_index]



                for y_scan_point in range(
                        y_scan_range_start, y_scan_range_stop):

                    left_data, right_data = self.comare_layers(
                        model_layer, y_scan_point)

                    distance_from_start_point_pixcels = y_scan_start_point - y_scan_point
                    total_y_distance_mm =start_hight_mm

                    for y_range in range(distance_from_start_point_pixcels):

                        y = y_scan_start_point - y_range
                        x = self.center_point_x_image

                        distance_1 = self.scan_data[y][x]
                        distance_2 = self.scan_data[y - 1][x]

                        z1 = int(distance_1)
                        z2 = int(distance_2)
                        change_in_distance = z1 - z2

                        if change_in_distance>self.z_axies_error_margion:
                            z1=z1+change_in_distance/2

                        total_y_distance_mm = total_y_distance_mm + \
                            self.y_pixel_to_mm(z1, 1)

                    layer_hight_mm = model_layer
                    if total_y_distance_mm > layer_hight_mm - \
                            self.y_axies_margtion_for_error and total_y_distance_mm < layer_hight_mm + self.y_axies_margtion_for_error:



                        if  comapre_results[model_layer][0]==False:
                            comapre_results[model_layer] = [
                                True,left_data, right_data]
                            if teast_mode:
                                cv2.line(self.couler_vesion_of_scan, (self.center_point_x_image, y_scan_point),
                                         (self.center_point_x_image + 10, y_scan_point), (255, 0, 0), 1)
                        else:
                            current_postive_match = 0
                            for vaule in comapre_results[model_layer][1]:
                                if vaule==False:
                                    current_postive_match = current_postive_match + 1

                            scan_match = 0
                            for vaule in left_data:
                                if vaule==False:
                                    scan_match = scan_match + 1

                            for vaule in right_data:
                                if vaule==False:
                                    scan_match = scan_match + 1

                            if scan_match > current_postive_match:
                                comapre_results[model_layer] = [
                                    True,left_data,right_data]
            if teast_mode:
                self.display_data("aaa",0)
            return comapre_results

        def count_index_blelow_vasule(hight):
            largest_index = 0
            index_count = -1
            for vaule in self.z_point_from_model:
                index_count += 1
                if vaule < hight:
                    if index_count > largest_index:
                        largest_index = index_count
            return largest_index


        start_hight = 0
        while True:
            hight,time_stamp = self.current_print_hight()
            if not  hight > self.start_scan_at:
                print("object orint not hight enofe yet")
                continue
            else:
                start_hight = hight
                time.sleep(2)
                load_scan_at_set_time(time_stamp)
                current_hight = hight
                break

        #jump to time

       # load_scan_at_set_time(time.time()-10)
       #  cv2.line(self.couler_vesion_of_scan, (self.center_point_x_image, 0),
       #           (self.center_point_x_image, 300), (255, 0, 0), 2)
       #  self.display_data("base_line", 0)

        while True:

            hight,time_stamp = self.current_print_hight()

            if hight > current_hight:
                time.sleep(2)
                load_scan_at_set_time(time_stamp)
                current_hight = hight


            comapre_results={}
            for full_model in range(0,count_index_blelow_vasule(hight)):
                model_layer = self.z_point_from_model[full_model]
                comapre_results[model_layer] = [
                    False, [
                        True, True, True], [
                        True, True, True]]


            base_model_point = 20
            any_point_found=False
            while True:
                #print("base_model_point",base_model_point)
                y_start = find_layer_0(base_model_point)
                if y_start !=9999:
                    print("start_hight",start_hight)
                    start_hight=self.z_point_from_model[base_model_point]


                    any_point_found=True
                    break
                base_model_point=base_model_point+1
                if base_model_point==len(self.z_point_from_model):
                    break
            print("base_model_point",base_model_point)
            if any_point_found==True:
                print("y_start", y_start)



                curent_distance=self.scan_data[y_start][self.center_point_x_image]
                curent_distance=curent_distance-5
                top_of_model_offste = self.y_mm_to_pixel(
                    curent_distance, hight)

                y_scan_range = y_start - (top_of_model_offste), y_start



                model_range = base_model_point, count_index_blelow_vasule(hight)
    # (y_scan_range,model_scan_range,y_scan_start_point,start_hight)
                out_data=compare_models(y_scan_range,model_range, y_start, start_hight,comapre_results)


            if any_point_found==False:
                print("full fail ")
                out_data= comapre_results
                model_range=0,count_index_blelow_vasule(hight)
                y_scan_range=0,0

            file_name="results "+self.current_file_name[0:-4]
            print("file_name",file_name)
            print("out_data",out_data)
            file=open(file_name,"w")
            for data in out_data:

                file.write(str(data)+"\n")

                file.write("layer_found"+str(out_data[data][0]) + "\n")

                out="left results"+str(out_data[data][1][0])+" "+str(out_data[data][1][1])+" "+str(out_data[data][1][2])+"\n"
                file.write(out)

                out = "right results" +str(out_data[data][2][0])+" "+str(out_data[data][2][1])+" "+str(out_data[data][2][2])+"\n"
                file.write(out)

                out = "range_moele_results " +str(model_range[0])+" "+str(model_range[1])+"\n"
                file.write(out)

                out = "range_yscan_results " + str(y_scan_range[0]) + " " + str(y_scan_range[1]) + "\n"
                file.write(out)

                file.write("\n\n")

            file.close()
            print("geting next scan ")

            get_next_scan()


    def draw_line(self,start,couler=(0,0,255),size=1):


        cv2.line(self.couler_vesion_of_scan, start, (start[0],start[1]+10), couler, size)



    def display_data(self,name="",dely=50):
        cv2.imshow(name, self.couler_vesion_of_scan)
        name=name+".png"
        cv2.imwrite(name,self.couler_vesion_of_scan)
        cv2.waitKey(dely)
        cv2.destroyAllWindows()

        couler_vesion_of_scan = np.copy(self.scan_data)
        couler_vesion_of_scan = couler_vesion_of_scan.astype(np.uint8)
        self.couler_vesion_of_scan = cv2.cvtColor(couler_vesion_of_scan, cv2.COLOR_GRAY2RGB)

dir_of_scan_data="D:/scan_notes/teast13/"
#dir_code_gcode="C:/Users/back up/Documents/GitHub/honner-progect/final_code/gcode_recve/time_layer_data"
dir_code_gcode="./time_layer_data"
temp=main_class(dir_of_scan_data, dir_code_gcode)
temp.load_in_perfect_model()
temp.find_first_scan()
temp.main_compare()