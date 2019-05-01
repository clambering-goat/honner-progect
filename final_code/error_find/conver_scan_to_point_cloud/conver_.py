

import numpy as np



scan_data=np.load("scan_part_2_at_angle.npy")


center_point_x_image = 355



def x_pixel_to_mm( distance_to_object_mm, number_of_pixels):
    mm_size = (distance_to_object_mm / 1000) * 1.7 * number_of_pixels
    return mm_size



def y_pixel_to_mm( distance_to_object_mm, number_of_pixels):
    mm_size = (distance_to_object_mm / 1000) * 1.64 * number_of_pixels
    return mm_size


point_could=[]

current_y_pos=0
for h in range(260, 325):
    current_x_pos = 105

    z_1_t = scan_data[h][355]
    z_2_t = scan_data[h+1][355]
    z1=int(z_1_t)
    z2=int(z_2_t)
    change_in_distace = (z1 - z2)

    if change_in_distace < 5:
        change_in_distace = z1
    else:
        change_in_distace = z1 + change_in_distace / 2

    current_y_pos=current_y_pos+y_pixel_to_mm(change_in_distace,1)
    point_could.append((current_x_pos, 0, current_y_pos))
    # for w_r in range(317,355):
    #
    #
    #     z_1_t = scan_data[h][w_r]
    #     z_2_t = scan_data[h][w_r+1]
    #     z1 = int(z_1_t)
    #     z2 = int(z_2_t)
    #     change_in_distace = (z1 - z2)
    #
    #     if change_in_distace < 5:
    #         change_in_distace = z1
    #     else:
    #         change_in_distace = z1 + change_in_distace / 2
    #
    #     current_x_pos=current_x_pos+x_pixel_to_mm(change_in_distace,1)
    #     current_x_pos=105-current_x_pos
    #
    #     point_could.append((current_x_pos,current_y_pos,0))





    current_x_pos = 0
    for w_l in range(38):

        w_l=355-w_l
        z_1_t = scan_data[h][w_l]
        z_2_t = scan_data[h][w_l-1]

        if z_1_t<1020 and z_1_t>610 and z_2_t<1020 and z_2_t>610:

            z1 = int(z_1_t)
            z2 = int(z_2_t)
            change_in_distace = (z1 - z2)

            if change_in_distace < 5:
                change_in_distace = z1
            else:
                change_in_distace = z1 + change_in_distace / 2

            current_x_pos = current_x_pos + x_pixel_to_mm(change_in_distace, 1)
            current_x_pos_mm = 105 - current_x_pos

            point_could.append((current_x_pos_mm,0, current_y_pos))



    current_x_pos = 0
    for w_l in range(355, 395):


        z_1_t = scan_data[h][w_l]
        z_2_t = scan_data[h][w_l+1]

        if z_1_t<1020 and z_1_t>610 and z_2_t<1020 and z_2_t>610:

            z1 = int(z_1_t)
            z2 = int(z_2_t)
            change_in_distace = (z1 - z2)

            if change_in_distace < 5:
                change_in_distace = z1
            else:
                change_in_distace = z1 + change_in_distace / 2

            current_x_pos = current_x_pos + x_pixel_to_mm(change_in_distace, 1)
            current_x_pos_mm = 105 + current_x_pos

            point_could.append((current_x_pos_mm,0 , current_y_pos))





file=open("remmade_point_cloud.txt","w")

for q in point_could:
    data=str(q[0])+" "+str(q[1])+" "+str(q[2])+"\n"
    file.write(data)

file.close()