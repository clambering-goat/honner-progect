


#

import os
import numpy as np
import cv2

class compare:
    def __init__(self):


        self.printer_center_x=105

        self.center_point_x_image = 357
        self.center_point_y_image = 269






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

    def draw_line(self,start,couler,size):


        cv2.line(self.couler_vesion_of_scan, start, (start[0],start[1]+10), couler, size)



    def display_data(self):
        cv2.imshow(" ", self.couler_vesion_of_scan)

        cv2.waitKey(0)
        cv2.destroyAllWindows()


temp=compare()
temp.load_in_data()
temp.display_data()

