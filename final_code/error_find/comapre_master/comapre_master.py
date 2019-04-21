

# set up and math used
import numpy as np
import cv2
import os
#import math



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


def find_smallest_x(array):
    smallest_x = 9999,0
    for points in array:
        x, y = points
        if x < smallest_x[0]:
            smallest_x = x,y

    return smallest_x



def find_largest_x(array):
    largest_x = -9999,0
    for points in array:
        x, y = points
        if x < largest_x[0]:
            largest_x = x,y

    return largest_x


#file find

numpy_file=""
MAX_point_file=""
y_over_x_file=""

for files in os.listdir("./"):
    if files[0:5]=="chane":
        y_over_x_file=files
    if files[-4:len(files)] == ".npy":
        numpy_file=files
    if files[0:5]=="x_max":
        MAX_point_file=files


print("nump file ",numpy_file)
print("y_over_x file ",y_over_x_file)
print("x max and min file ",MAX_point_file)




printer_center_x=105


#find the model 00 poinrts


data_input=np.load(numpy_file)
#data_input=np.load("match_scan.npy")


couler_vesion_on_data=np.copy(data_input)
couler_vesion_on_data=couler_vesion_on_data.astype(np.uint8)
couler_vesion_on_data = cv2.cvtColor(couler_vesion_on_data,cv2.COLOR_GRAY2RGB)



file=open(y_over_x_file,"r")
file_data=file.readlines()
file.close()

hight_point_in_model=[]
x_scan_across={}
for raw_data in file_data:

    x,y,z=raw_data.split(" ")
    x=float(x)
    y=float(y)
    z=float(z)

    if not z in x_scan_across.keys():
        x_scan_across[z]=[]
        hight_point_in_model.append(z)
    x_scan_across[z].append((x,y))








file=open(MAX_point_file,"r")
file_data=file.readlines()
file.close()
#line exasmeple
#124.8 125.2 85.2 75.2 105 125.2 1.3
#x_max=124.8 125.2
#x_min=85.2 75.2
#x_center=105 125.2
#current_hight_model=1.3

model_pixcel_size_at_given_hight={}
for x_max_data in file_data:
    split_data=x_max_data.split(" ")

    x_max_point=float(split_data[0])
    x_min_point=float(split_data[2])
    x_mid_point=float(split_data[4])
    current_hight_model=float(split_data[6])

    model_pixcel_size_at_given_hight[current_hight_model]=x_max_point,x_min_point,x_mid_point












center_point_x_image=357
center_point_y_image=269

cv2.line(couler_vesion_on_data, (center_point_x_image, center_point_y_image), (center_point_x_image, center_point_y_image - 20), (255, 0, 0), 2)

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

    y_point= center_point_y_image + looking_y_vaules
    distance_vaule_from_scan=data_input[y_point][center_point_x_image]

    if distance_vaule_from_scan>min_distance and distance_vaule_from_scan <max_distance:

        print("top of model found at :", center_point_x_image, y_point)
        midle_distance_vaule=distance_vaule_from_scan
        break

print("midle distance vaule is ",midle_distance_vaule)

distance_to_base_pixes=y_mm_to_pixel(midle_distance_vaule,distance_to_base_mm)




model_00_point_pixcels= center_point_x_image, center_point_y_image + distance_to_base_pixes, data_input[center_point_y_image + distance_to_base_pixes - 2][center_point_x_image]


print("base is at point ", model_00_point_pixcels)


#simple scan lef and right to find any poin that might be the model
#scan left


current_hight_model=hight_point_in_model[50]

print("comparing at higth MM  ", current_hight_model)


#conver model hight to pixels hight
start_vaule=current_hight_model
compare_pixle_hight=0
offset=0

while True:
    offset+=1

    distance=data_input[model_00_point_pixcels[1] - offset][model_00_point_pixcels[0]]

    start_vaule=start_vaule-y_pixel_to_mm(distance,1)
    if start_vaule<0:
        break
    compare_pixle_hight+=1

print("the pixcel highit is ",compare_pixle_hight)



X_max_p,X_min_p,x_mid_p=model_pixcel_size_at_given_hight[current_hight_model]


x_min_size_mm=abs(X_min_p-x_mid_p)
x_max_size_mm=abs(X_max_p-x_mid_p)


offset=0
start_vaule=x_min_size_mm
X_min_size_pixels=0
print("modle x min is mm of center ",start_vaule)
while True:
    offset+=1

    y= model_00_point_pixcels[1] - compare_pixle_hight
    x= model_00_point_pixcels[0] - offset
    distance=data_input[y][x]

    start_vaule=start_vaule-x_pixel_to_mm(distance,1)
    X_min_size_pixels += 1
    if start_vaule<0:
        break


print("x_min size in pixcels ",X_min_size_pixels)


offset=0
start_vaule=x_max_size_mm
print("modle x max is mm of center ",start_vaule)
X_max_size_pixels=0
while True:
    offset+=1
    y= model_00_point_pixcels[1] - compare_pixle_hight
    x= model_00_point_pixcels[0] + offset
    distance=data_input[y][x]

    x_mm=x_pixel_to_mm(distance, 1)
    start_vaule=start_vaule-x_mm
    X_max_size_pixels += 1

    if start_vaule<0:
        break


print("x_max size in pixcels ",X_max_size_pixels)


#cv2.line(couler_vesion_on_data, (center_point_x_image, center_point_y_image), (center_point_x_image+X_max_size_pixels, center_point_y_image ), (125, 0, 0), 2)
#cv2.line(couler_vesion_on_data, (center_point_x_image, center_point_y_image), (center_point_x_image-X_min_size_pixels, center_point_y_image ), (125, 0, 0), 2)










point_from_model=x_scan_across[current_hight_model]



#center_out
x_center_out_x_min=[]
for points in point_from_model:
    x,y=points
    if x==printer_center_x:
        x_center_point_from_models=points

        break




#center_out
x_center_out_x_min=[]
for points in point_from_model:
    x,y=points
    if x<printer_center_x:

        x_center_out_x_min.append(points)







x_center_out_x_max=[]
for points in point_from_model:
    x,y=points
    if x>printer_center_x:

        x_center_out_x_max.append(points)





#scan right



shift=0



over_size=False
under_size=True

old_point_from_scan= model_00_point_pixcels[0], model_00_point_pixcels[1] - compare_pixle_hight, model_00_point_pixcels[2]



#get the next point

#cold start problem
next_point_from_models=x_center_point_from_models
old_point_from_models=0,0

model_x_distance=0
model_y_distance=0
total_y_scan_distance=0

move_to_next_point_in_model=False
print("start point scan pixles", old_point_from_scan)

print("start model from models,x",printer_center_x)

vaild_y_x_point_found=0
invasile_y_x_points_found=0
end_of_x_comare_to_y=False
ditace_from_center_mm=printer_center_x

while True:

    shift+=1
    y= model_00_point_pixcels[1] - compare_pixle_hight
    x= model_00_point_pixcels[0] + shift
    print("x,y",x,y)

    if x+1>len(data_input[0]):
        print("point out of bond in the x axies ")
        break

    distance_vaule_from_scan = data_input[y][x]




    if  distance_vaule_from_scan < min_distance or distance_vaule_from_scan > max_distance:
        print("invail depth vaule found at ",x,y)
        print("distance vasule ",distance_vaule_from_scan )

        break


    picels_error_margion=2
    #see if miodele to small

    if shift>X_max_size_pixels-picels_error_margion and shift<X_max_size_pixels+picels_error_margion:
        under_size=False

    #see if model to big
    if shift>X_max_size_pixels+picels_error_margion:
        print("shift ",shift)
        print("X_max_size_pixels",X_max_size_pixels)
        over_size=True




    current_point = x,y, distance_vaule_from_scan








    #slove werid numpy vaule math thing
    current_z_pos=int(current_point[2])
    old_z_pos=int(old_point_from_scan[2])





    #p2-p1

    change_in_distance= (current_z_pos-old_z_pos)

    #x_changin from models scan

    total_y_scan_distance+=change_in_distance




    if change_in_distance>5:
        distance=current_z_pos+change_in_distance/2
    else:
        distance=current_z_pos

    print("distance",distance)
    print("one pixel is mm ",x_pixel_to_mm(distance,1))



    ditace_from_center_mm=ditace_from_center_mm+x_pixel_to_mm(distance,1)


    #need to fix as one picel is 1.2 mm each loop the models move 1mm the image moves 1.2 ]#



    for vauls in x_center_out_x_max:
        x_t,y_t=vauls
        if  x_t>ditace_from_center_mm-0.01 and  x_t<ditace_from_center_mm+0.01:
            old_point_from_models = next_point_from_models
            next_point_from_models=vauls
            break




    print("except change ",model_y_distance)
    print("got change ",change_in_distance)

    print("model point comaper")
    print(old_point_from_models)
    print()



    x1,y1=old_point_from_models
    x2,y2=next_point_from_models

    model_x_distance=x2-x1
    #note to cheek
    model_y_distance=(y2-y1)
    model_y_distance=(model_y_distance)

    if change_in_distance>=model_y_distance-1 and  change_in_distance <=model_y_distance+1:


        start_point=x,y
        end_point=x,y-10

        cv2.line(couler_vesion_on_data, start_point,end_point, (0, 255, 0), 1)

        vaild_y_x_point_found+=1
    else:
        start_point=x,y
        end_point=x,y-10

        cv2.line(couler_vesion_on_data, start_point,end_point, (0, 0, 255), 1)

        invasile_y_x_points_found+=1


    #
    # if len(x_center_out_x_max)==0:
    #     end_of_x_comare_to_y=True
    # else:
    #     old_point_from_models=next_point_from_models
    #     next_point_from_models = find_smallest_x(x_center_out_x_max)
    #
    #
    #     x_center_out_x_max.remove(next_point_from_models)
    #
    #     x1,y1=old_point_from_models
    #     x2,y2=next_point_from_models
    #
    #     model_x_distance=x2-x1
    #     #note to cheek
    #     model_y_distance=(y2-y1)
    #     model_y_distance=int(model_y_distance)
    #
    #     total_y_scan_distance=0
    #
    # #print(change_in_distance)
    #
    #
    old_point_from_scan=current_point



print("-------------------------")
print("results ")

print("over_size",over_size)

print("under_size",under_size)
print("vaild_y_x_point_found",vaild_y_x_point_found)
print("invasile_y_x_points_found",invasile_y_x_points_found)


cv2.imshow("midle_points",couler_vesion_on_data)

cv2.waitKey(0)
cv2.destroyAllWindows()








print("")











''' 

left_shift=0
while True:
    left_shift+=1
    distance_vauls=data_input[model_00_point_pixcels[1]][model_00_point_pixcels[0]-left_shift]
    if distance_vauls>max_distance or distance_vauls<min_distance:

        left_shift=left_shift-1
        print("left edge found at ",left_shift,"from center ")
        print("next ditacne vaule is ",distance_vauls)
        break

right_shift=0

while True:
    right_shift+=1
    distance_vauls=data_input[model_00_point_pixcels[1]][model_00_point_pixcels[0]+right_shift]
    if distance_vauls>max_distance or distance_vauls<min_distance:
        right_shift =right_shift-1
        print("left edge found at ",right_shift,"from center ")
        break




# get the x size from file and conver to pixels size from  center


cv2.line(couler_vesion_on_data, (model_00_point_pixcels[0]+right_shift,model_00_point_pixcels[1]), model_00_point_pixcels, (255, 0, 0), 2)
cv2.line(couler_vesion_on_data, (model_00_point_pixcels[0]-left_shift,model_00_point_pixcels[1]), model_00_point_pixcels, (0, 0, 255), 2)
'''



''' 

#chane_y_over_xpoint_cloud_of_changin_in_depth_teast.txt

file=open("x_max_minpoint_cloud_of_changin_in_depth_teast.txt","r")

#line exasmeple
#124.8 125.2 85.2 75.2 105 125.2 1.3
#x_max=124.8 125.2
#x_min=85.2 75.2
#x_center=105 125.2
#current_hight_model=1.3

model_pixcel_size_at_given_hight={}
for x_max_data in file_data:
    split_data=x_max_data.split(" ")

    x_max_point=float(split_data[0]),float(split_data[1])
    x_min_point=float(split_data[2]),float(split_data[3])
    x_mid_point=float(split_data[4]),float(split_data[5])
    current_hight_model=float(split_data[6])

    print("find max and min for current_hight_model ",current_hight_model)
    model_pixcel_size_at_given_hight[current_hight_model]=x_max_point,x_min_point,center_point_x_image











#line exasmeple
#x,y,z
#86 94.8 1.3


'''







