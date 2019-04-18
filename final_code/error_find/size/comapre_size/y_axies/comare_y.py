import numpy as np
import cv2



file_to_open="chane_y_over_xpoint_cloud_of_changin_in_depth_teast.txt"





data_input=np.load("data_2.npy")
center_point= 335, 269


back_up=np.copy(data_input)
back_up=back_up.astype(np.uint8)
back_up = cv2.cvtColor(back_up,cv2.COLOR_GRAY2RGB)
line_start=center_point
line_end=int(center_point[0]),int(center_point[1]+20)


def x_pixel_to_mm(distance_to_object_mm,number_of_pixels):
    mm_size = (distance_to_object_mm / 1000) * 1.7 * number_of_pixels
    return mm_size






cv2.line(back_up, line_start, line_end, (255, 0, 0), 2)




file=open(file_to_open,"r")
file_data=file.readlines()
file.close()



diatnce_bwtween_points_pixels=1

old_point=0,0,0

sacn_start=-16
end_scan=18
change_in_z=0

toatal_x_size_mm=0

for q in range(sacn_start,end_scan,diatnce_bwtween_points_pixels):

    diatnce_at_point = data_input[line_start[1]][line_start[0]+q]

    if q ==sacn_start:

        old_point=line_start[0],line_start[1],diatnce_at_point
        print("hi")
        continue


    #do thing
    current_point=line_start[0]+q,line_start[1],diatnce_at_point



    chan_in_x=diatnce_bwtween_points_pixels
    changing_in_y=0
    #p2-p1
    current_z_pos=int(current_point[2])
    old_z_pos=int(old_point[2])

    print("v1 ", current_z_pos)
    print("v2 ", old_z_pos)
    print("v3 ", old_z_pos - current_z_pos)



    #p2-p1

    change_in_z= (old_z_pos - current_z_pos)

    half_way=change_in_z/2
    half_way=half_way+old_z_pos

    if abs(change_in_z)>5:


        x_MM=x_pixel_to_mm(half_way, diatnce_bwtween_points_pixels)

    else:
        x_MM=x_pixel_to_mm(current_z_pos, diatnce_bwtween_points_pixels)

    toatal_x_size_mm+=x_MM



    #end of thing

    old_point = line_start[0], line_start[1], diatnce_at_point


    print(" distance vaule ",diatnce_at_point)
    print("change distance vaule ", change_in_z)

    cv2.line(back_up, line_start, (line_start[0]+q,line_start[1]), (255, 0, 0), 2)

print(toatal_x_size_mm)











data_input=data_input.astype(np.uint8)

cv2.imshow("frame2",back_up)
cv2.imshow("frame",data_input)

cv2.waitKey(0)
cv2.destroyAllWindows()


