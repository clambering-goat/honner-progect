

import numpy as np
import cv2

data_input=np.load("data_2.npy")
center_point= 335, 269


back_up=np.copy(data_input)
back_up=back_up.astype(np.uint8)
back_up = cv2.cvtColor(back_up,cv2.COLOR_GRAY2RGB)



file=open("x_max_min.txt","r")

file_data=file.readlines()
file.close()

distance_to_base_mm=31.58

z_dixstance_at_center_mm= (data_input[center_point[1]][center_point[0]])

print("center vaiuke ",z_dixstance_at_center_mm)

distance_to_base_pixels=distance_to_base_mm/(1.64*(z_dixstance_at_center_mm/1000))
distance_to_base_pixels=round(distance_to_base_pixels)



def round_and_int(vaule):
    vaule=float(vaule)
    vaule=round(vaule)
    vaule=int(vaule)
    return vaule



#size at base


master_pass=True

for aaa in range(2,30):
    look_at_hight=aaa
    error_margion=0.2


    #find hight vaule in the file
    matching_x_vaules={}
    for data in file_data:
        #exsample
        #p1 124.8 125.2
        #p2 85.2 94.8
        # center 134.8
        #hight 3.1

        max_x_mm,max_x_mm_y, min_x_mm,min_x_mm_y,y_center_vaule ,z_pos_mm=data.split(" ")


        max_x_mm=float(max_x_mm)
        max_x_mm_y=float(max_x_mm_y)

        min_x_mm=float(min_x_mm)
        min_x_mm_y=float(min_x_mm_y)

        y_center_vaule=float(y_center_vaule)

        z_pos_mm=float(z_pos_mm)

        if z_pos_mm >= look_at_hight-error_margion and z_pos_mm<= look_at_hight+error_margion:
            print("found hight in file")
            print(z_pos_mm)

            #comerver mm to pixels

            max_size_mm=max_x_mm-min_x_mm


            #add z fact ing conpoints

            changin_in_y_1=max_x_mm_y-y_center_vaule

            changin_in_y_2=min_x_mm_y-y_center_vaule

            

            max_size_pixsel=max_size_mm/(1.7*(z_dixstance_at_center_mm/1000))




            max_x_pixel = ((max_size_pixsel)/2)
            min_x_pixel = ((max_size_pixsel)/2)

            max_x_pixel=round_and_int(max_x_pixel)
            min_x_pixel=round_and_int(min_x_pixel)


            z_pos_pixels=z_pos_mm/(1.64*(z_dixstance_at_center_mm/1000))

            matching_x_vaules[z_pos_pixels]= max_x_pixel, min_x_pixel



    #comare x measure from file to scan vaules
    x_max_wiggle_room=False
    x_min_wiggle_room=False

    for give_hight in matching_x_vaules:

        max_x_pixel, min_x_pixel=matching_x_vaules[give_hight]


        for x_wiggle in range(-5,5):
            point_y=int((center_point[1] + distance_to_base_pixels)-give_hight)

            x_max_postion_to_look= max_x_pixel + x_wiggle+center_point[0]
            x_min_postion_to_look= x_wiggle+center_point[0]-min_x_pixel


            comapre_vaule_x_max=data_input[point_y][x_max_postion_to_look]
            comapre_vaule_x_min=data_input[point_y][x_min_postion_to_look]



            #reoced wher they sacn
            cv2.line(back_up, (x_max_postion_to_look, point_y), (x_max_postion_to_look, point_y), (255, 0, 0), 2)
            cv2.line(back_up, (x_min_postion_to_look, point_y), (x_min_postion_to_look, point_y), (0, 0, 255), 2)

            z_dixstance_to_Comare=700
            range_of_vaule=90

            if comapre_vaule_x_max >z_dixstance_to_Comare-range_of_vaule and comapre_vaule_x_max <=z_dixstance_to_Comare+range_of_vaule:
                x_max_wiggle_room=True

            if comapre_vaule_x_min > z_dixstance_to_Comare - range_of_vaule and comapre_vaule_x_min <= z_dixstance_to_Comare + range_of_vaule:
                x_min_wiggle_room = True

    print(x_max_wiggle_room,x_min_wiggle_room)
    if x_max_wiggle_room==False or x_min_wiggle_room==False:
        master_pass=False



print("master pass is ",master_pass)




line_start=center_point
line_end=int(center_point[0]),int(center_point[1]+distance_to_base_pixels)




data_input=data_input.astype(np.uint8)



cv2.line(back_up, line_start, line_end, (255, 0, 0), 2)


cv2.imshow("frame2",back_up)
cv2.imshow("frame",data_input)

cv2.waitKey(0)
cv2.destroyAllWindows()






