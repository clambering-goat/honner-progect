

import numpy as np
import cv2

data_input=np.load("data_2.npy")
given_center_point=335, 269




z_offster_from_cal_file=31.58





given_z_dixstance= (data_input[given_center_point[1]][given_center_point[0]])

start_pixsel_y_offste=z_offster_from_cal_file/(1.64*(given_z_dixstance/1000))


start_0_0_point=int(given_center_point[0]),int(given_center_point[1]+start_pixsel_y_offste)



print("starting at points ", start_0_0_point)

print("given z distance",given_z_dixstance)

def get_y_center_pount(z_distance):

    new_pixesl_offset=z_offster_from_cal_file/(1.64*(z_distance/1000))
    new_pixesl_offset=int(new_pixesl_offset)
    return new_pixesl_offset



def get_x_size(z_distance):

    pixel_size=30/(1.7*(z_distance/1000))
    pixel_size=pixel_size
    return pixel_size

match = 0
no_match = 0

back_up=np.copy(data_input)


#right cheek
for q in range(start_0_0_point[0]-80,start_0_0_point[1]):



    pixel_size=get_x_size(given_z_dixstance)

    match_in_x_wiggle_room=False
    for w in range(-5,5):
        offset=pixel_size+w
        x_look=int(given_center_point[0]+offset)
        y_look=q



        comapre_vaule=data_input[y_look][x_look]

        data_input[y_look][x_look]=0
        print("comapre",comapre_vaule)
        print("vaule",given_z_dixstance)
        print(" ")

        if comapre_vaule >given_z_dixstance-10 and comapre_vaule <=given_z_dixstance+5:
            match_in_x_wiggle_room=True



    if match_in_x_wiggle_room:

        match+=1
    else:
        no_match+=1



#left cheek


for q in range(start_0_0_point[0] - 80, start_0_0_point[1]):

    pixel_size = get_x_size(given_z_dixstance)

    match_in_x_wiggle_room = False
    for w in range(-5, 5):
        offset = pixel_size + w
        x_look = int(given_center_point[0] - offset)
        y_look = q

        comapre_vaule = data_input[y_look][x_look]

        data_input[y_look][x_look] = 0
        print("comapre", comapre_vaule)
        print("vaule", given_z_dixstance)
        print(" ")

        if comapre_vaule > given_z_dixstance - 10 and comapre_vaule <= given_z_dixstance + 5:
            match_in_x_wiggle_room = True

    if match_in_x_wiggle_room:

        match += 1
    else:
        no_match += 1

print("match",match)
print("no match",no_match)
data_input=data_input.astype(np.uint8)


back_up=back_up.astype(np.uint8)

cv2.imshow("frame2",back_up)

data_input = cv2.cvtColor(data_input,cv2.COLOR_GRAY2RGB)

cv2.line(data_input,given_center_point,(start_0_0_point),(255,0,0),2)

cv2.imshow("frame",data_input)

cv2.waitKey(0)

cv2.destroyAllWindows()


print("match",match)
print("no match",no_match)




