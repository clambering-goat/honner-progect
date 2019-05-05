


import os
import cv2
import numpy as np
import time
where_to_look="./"


def find_latest_scan(where_to_look):
    while True:
        current_file=""
        bigest_file=0
        for files in os.listdir(where_to_look):
            if files[0:13] == "results depth":

                raw_sting=files.split(" ")
                raw_sting=raw_sting[-1]
                raw_sting=raw_sting.split(".")
                time_v=int(raw_sting[0])

                if time_v >bigest_file:
                    bigest_file=time_v
                    current_file=files

        if current_file=="":
            print("no fiile found")
            time.sleep(10)
        else:
            return current_file
    #current_file="results depth_carmea('192.168.1.227', 54462)_10391 1556836371.7497523"




def load_scan_data(where_to_look,current_file):
    current_file=current_file[8:]
    current_file=current_file+".npy"
    print("current_file",current_file)

    file_to_load = (where_to_look + current_file)

    scan_data = np.load(file_to_load)

    couler_vesion_of_scan = np.copy(scan_data)
    couler_vesion_of_scan = couler_vesion_of_scan.astype(np.uint8)
    couler_vesion_of_scan = cv2.cvtColor(
        couler_vesion_of_scan, cv2.COLOR_GRAY2RGB)

    return couler_vesion_of_scan



def displayer_results(file_name):

    print("opening file ",file_name,"\n")

    image_data=load_scan_data("D:/scan_notes/square_teast_2/", file_name)

    blank_image=np.zeros((400,400,3),dtype=np.uint8)
    file=open(file_name,"r")
    data=file.read()
    file.close()
    reults=data.split("\n\n")

    reults=reults[0:-1]

    reulats_data={}

    line_info=reults[0]
    line_info=line_info.split("\n")
    hight = line_info[0]

    layer_found = line_info[1]
    left_result = line_info[2]
    right_results = line_info[3]


    reulats_data[hight] = layer_found, left_result, right_results

    for info in reults[1:]:
        line_info = info.split("\n")
        line_info=line_info[1:]
        hight = line_info[0]

        layer_found = line_info[1]
        left_result = line_info[2]
        right_results = line_info[3]
        reulats_data[hight]=layer_found,left_result,right_results



    file=open("x_max_min_point_cloud_of_wall_teast__.txt","r")

    data=file.readlines()
    file.close()



    loop_counter=-1
    start_point=200
    for q in data:
        loop_counter=loop_counter+1

        split_data = q.split(" ")

        start=float(split_data[0]),float(split_data[-1])
        start=int(start[0]),start_point-int(start[1])


        end = float(split_data[2]), float(split_data[-1])
        end=int(end[0]),start_point-int(end[1])

        center_point_temp=float(split_data[4]),float(split_data[-1])

        center_point=int(center_point_temp[0]),start_point-int(center_point_temp[1])
        if center_point_temp[1]>40:
            print()
        if split_data[-1].strip() in reulats_data.keys():
            info=reulats_data[split_data[-1].strip()]

            if info[0]=="layer_foundTrue":

                #left
                sub_reuluts=info[1].split(" ")
                if info[1]=="left resultsFalse False False":
                    cv2.line(blank_image, end, center_point, (0, 255, 0), 1)

                if sub_reuluts[1]=="resultsTrue":
                    cv2.line(blank_image, end, center_point, (255, 0, 255), 1)

                if sub_reuluts[2]=="True":
                    cv2.line(blank_image, end, center_point, (255, 0, 0), 1)

                if sub_reuluts[3]=="True":
                    cv2.line(blank_image, end, center_point, (255, 255, 0), 1)


                #right
                #full match
                sub_reuluts = info[2].split(" ")
                if info[2] == "right resultsFalse False False":
                    cv2.line(blank_image, start,center_point, (0, 255, 0), 1)
                if sub_reuluts[1]=="resultsTrue":
                    cv2.line(blank_image, start, center_point, (255, 0, 255), 1)

                if sub_reuluts[2]=="True":
                    cv2.line(blank_image, start, center_point, (255, 0, 0), 1)

                if sub_reuluts[3]=="True":
                    cv2.line(blank_image, start, center_point, (255, 255, 0), 1)


            if info[0]=="layer_foundFalse":
                cv2.line(blank_image, start, end, (0, 0, 255), 1)

            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (200, 100)
            fontScale = 1
            fontColor = (255, 0, 255)
            lineType = 2

            cv2.putText(blank_image, 'under_size',
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)

            fontColor=(255, 0, 0)
            bottomLeftCornerOfText = (200, 150)
            cv2.putText(blank_image, 'over_size',
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)

            fontColor=(255, 255, 0)
            bottomLeftCornerOfText = (200, 200)
            cv2.putText(blank_image, 'z_not_matching',
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)


            fontColor=(0, 0, 255)
            bottomLeftCornerOfText = (200, 250)
            cv2.putText(blank_image, 'no_match',
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)

            fontColor=(0, 255, 0)
            bottomLeftCornerOfText = (200, 300)
            cv2.putText(blank_image, 'full_match',
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)

    cv2.imshow("scan_image",image_data)

    cv2.imshow("results ", blank_image)
    file_Save_name="./results/grafice_of_results"+file_name+".png"
    cv2.imwrite(file_Save_name,blank_image)
    cv2.waitKey(500)




while True:
    current_scan=find_latest_scan("./")

    displayer_results(current_scan)