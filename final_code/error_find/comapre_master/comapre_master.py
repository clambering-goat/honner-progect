

# set up and math used
import numpy as np
import cv2
import math

def x_pixel_to_mm(distance_to_object_mm,number_of_pixels):
    mm_size = (distance_to_object_mm / 1000) * 1.7 * number_of_pixels
    return mm_size


def x_mm_to_pixel(distance_to_object_mm, size_in_mm):
    pixels_size = size_in_mm / (1.7 * (distance_to_object_mm / 1000))
    return pixels_size




def y_pixel_to_mm(distance_to_object_mm, number_of_pixels):
    mm_size=(distance_to_object_mm / 1000)*1.64*number_of_pixels
    return mm_size



def y_mm_to_pixel(distance_to_object_mm, size_in_mm):
    pixels_size = size_in_mm / (1.64 * (distance_to_object_mm / 1000))
    pixels_size=round(pixels_size)
    pixels_size=int(pixels_size)
    return pixels_size




#find the model 00 poinrts
data_input=np.load("data_2.npy")


couler_vesion_on_data=np.copy(data_input)
couler_vesion_on_data=couler_vesion_on_data.astype(np.uint8)
couler_vesion_on_data = cv2.cvtColor(couler_vesion_on_data,cv2.COLOR_GRAY2RGB)


center_point_x=335
center_point_y=269

cv2.line(couler_vesion_on_data, (center_point_x,center_point_y), (center_point_x,center_point_y-20), (125, 0, 0), 2)

#max distance in the print bed
max_distance=1065
min_distance=655

#step_1 find the bottem point
#the calibation ditace from the point 269

distance_to_base_mm=31.58

max_distance_to_base_in_pixsels=y_mm_to_pixel(min_distance,distance_to_base_mm)
min_distance_to_base_in_pixsels=y_mm_to_pixel(max_distance,distance_to_base_mm)

print("max distance to print bed in pixels is ",max_distance_to_base_in_pixsels)
print("min distance to print bed in pixels is ",min_distance_to_base_in_pixsels)


midle_distance_vaule=0
y_sacn_range=max_distance_to_base_in_pixsels-min_distance_to_base_in_pixsels
print("the y_sacn_range ",y_sacn_range)


for looking_y_vaules in range(0,y_sacn_range,1):

    y_point=center_point_y+looking_y_vaules
    distance_vaule_from_scan=data_input[y_point][center_point_x]

    if distance_vaule_from_scan>min_distance and distance_vaule_from_scan <max_distance:

        print("top of model found at :", center_point_x,y_point)
        midle_distance_vaule=distance_vaule_from_scan
        break

print("midle distance vaule is ",midle_distance_vaule)

distance_to_base_pixes=y_mm_to_pixel(midle_distance_vaule,distance_to_base_mm)




model_00_point=center_point_x,center_point_y+distance_to_base_pixes

print("base is at point ",model_00_point)
cv2.line(couler_vesion_on_data, (center_point_x,center_point_y), model_00_point, (0, 255, 0), 2)




cv2.imshow("midle_points",couler_vesion_on_data)

cv2.waitKey(1000)
cv2.destroyAllWindows()



# load chang in y when mocving in x 



# get the x size from file and conver to pixels size from  center


file=open("x_max_minpoint_cloud_of_changin_in_depth_teast.txt","r")

file_data=file.readlines()
file.close()


#line exasmeple
#124.8 125.2 85.2 75.2 105 125.2 1.3
#x_max=124.8 125.2
#x_min=85.2 75.2
#x_center=105 125.2
#hight=1.3

for x_max_data in file_data:
    split_data=x_max_data.split(" ")

    x_max_point=float(split_data[0]),float(split_data[1])
    x_min_point=float(split_data[2]),float(split_data[3])
    x_mid_point=float(split_data[4]),float(split_data[5])
    hight=float(split_data[6])

    print("find max and min for hight ",hight)
    break


