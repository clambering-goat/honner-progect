

import numpy as np
import cv2
import os
from  math import tan ,degrees
#the object edge  is about 15cm from center


image_data=[]
depth_data=[]
print("files found ")
for q in os.listdir("./"):

    if q[-4:len(q)]==".npy":
        data=np.load(q)
        print(q)
        if q[0]=="c":
            image_data.append(data)
        if q[0]=="d":
            depth_data.append(data)


sensor_1=image_data[0],depth_data[0]
sensor_2=image_data[1],depth_data[1]



image_size=len(depth_data[0]),len(depth_data[0][0])
error_to_accept=10

print(image_size)









mid_y = int(image_size[0]/2)
mid_x = int(image_size[1]/2)
# get the data from the dethp image from sensor_1


def scan_for_object(sensor_to_use):
    sensor_depth=sensor_to_use[1]



    print("mid point of images")
    print("x ",mid_x)
    print("y ",mid_y)
    print(" ")

    sensor_mid_point=sensor_depth[mid_y][mid_x]

    print("sensor mid point vaule is ",sensor_mid_point)
    print("")




    def vertial_scan():
        start_point=mid_y
        constant_scan=mid_x

        last_scan_vaule=sensor_mid_point
        max_down = 0


        for scan_vaule in range(200):

            point_to_look_at=start_point-scan_vaule
            vaule_from_scan=sensor_depth[point_to_look_at][constant_scan]

            if vaule_from_scan>last_scan_vaule+error_to_accept or  vaule_from_scan<last_scan_vaule-error_to_accept:
                max_down = point_to_look_at + 1

                print("set max_down to ", max_down, "with vaule ", last_scan_vaule)
                print("vaule of next point", vaule_from_scan)
                print()
                break
            last_scan_vaule=vaule_from_scan



        last_scan_vaule=sensor_mid_point

        max_up=0

        for scan_vaule in range(200):

            point_to_look_at=start_point+scan_vaule
            vaule_from_scan=sensor_depth[point_to_look_at][constant_scan]

            if vaule_from_scan>last_scan_vaule+error_to_accept or  vaule_from_scan<last_scan_vaule-error_to_accept:
                max_up=point_to_look_at-1
                print("set max_up to ", max_up,"with vaule ",last_scan_vaule)
                print("vaule of next point", vaule_from_scan)
                print()
                break

            last_scan_vaule=vaule_from_scan

        return(max_down,max_up)



    def hozontail_scan():
        start_point=mid_x
        constant_scan=mid_y


        last_scan_vaule=sensor_mid_point

        max_right=0
        for scan_vaule in range(200):
            point_to_look_at=start_point+scan_vaule
            vaule_from_scan=sensor_depth[constant_scan][point_to_look_at]

            if vaule_from_scan>last_scan_vaule+error_to_accept or  vaule_from_scan<last_scan_vaule-error_to_accept:
                max_right=point_to_look_at-1

                print("set max_right to ",max_right,"with vaule ",last_scan_vaule)
                print("vaule of next point", vaule_from_scan)
                print()
                break
            last_scan_vaule=vaule_from_scan


        last_scan_vaule=sensor_mid_point

        max_left=0
        for scan_vaule in range(200):
            point_to_look_at=start_point-scan_vaule
            vaule_from_scan=sensor_depth[constant_scan][point_to_look_at]
            print(last_scan_vaule)
            if vaule_from_scan>last_scan_vaule+error_to_accept or  vaule_from_scan<last_scan_vaule-error_to_accept:
                max_left=point_to_look_at+1
                print("set max_left to ",max_left,"with vaule ",last_scan_vaule)
                print("vaule of next point", vaule_from_scan)
                print()
                break

            last_scan_vaule=vaule_from_scan

        return(max_left,max_right)

    hozontail_points=hozontail_scan()
    vertial_points=vertial_scan()

    return(hozontail_points,vertial_points)






def grafic_veiw():
    cv2.line(sensor_1[1],(mid_x,sensor_1_object_y_range[0]),(mid_x,sensor_1_object_y_range[1]),(125,0,125),5)
    cv2.line(sensor_1[1],(sensor_1_object_x_range[0],mid_y),(sensor_1_object_x_range[1],mid_y),(125,0,125),5)

    cv2.imshow('image',sensor_1[1])
    cv2.waitKey(0)



    cv2.line(sensor_2[1],(mid_x,sensor_2_object_y_range[0]),(mid_x,sensor_2_object_y_range[1]),(125,0,125),5)
    cv2.line(sensor_2[1],(sensor_2_object_x_range[0],mid_y),(sensor_2_object_x_range[1],mid_y),(125,0,125),5)

    cv2.imshow('image',sensor_2[1])
    cv2.waitKey(0)





    cv2.destroyAllWindows()



sensor_1_object_x_range,sensor_1_object_y_range=scan_for_object(sensor_1)

sensor_2_object_x_range,sensor_2_object_y_range=scan_for_object(sensor_2)


print("object x range sensor 1 ",sensor_1_object_x_range)
print("object y range sensor 1",sensor_1_object_y_range)

print("object x range sensor 2",sensor_2_object_x_range)
print("object y range sensor 2",sensor_2_object_y_range)

grafic_veiw()




def get_angle_to_target_x_axies(sensor_object,sensor):
    print("x axises rotation")
    point_in_sacn=[]
    temp=[]
    for q in range(sensor_object[0],sensor_object[1]):

        temp.append(q)
        #print((sensor[1][mid_y][point]))
        point_in_sacn.append(sensor[1][mid_y][q])


    A = np.vstack([temp, np.ones(len(temp))]).T
    m, c = np.linalg.lstsq(A,point_in_sacn,rcond=None)[0]

    print(m,c)

    print("y=",m,"x","+",c)
    anngel_to_tageget=tan(m)
    print("angle to the taget is radians  ",anngel_to_tageget)
    anngel_to_tageget=degrees(anngel_to_tageget)
    print("angle to the taget is degrees  ",anngel_to_tageget)

    print(" ")
    return(anngel_to_tageget,c)

def get_angle_to_target_y_axies(sensor_object,sensor):
    print("y axises rotation")
    point_in_sacn=[]
    temp=[]
    for q in range(sensor_object[0],sensor_object[1]):


        temp.append(q)
        #print("adding vauel main ",sensor[1][point][mid_x])
        point_in_sacn.append(sensor[1][q][mid_x])


    A = np.vstack([temp, np.ones(len(temp))]).T
    m, c = np.linalg.lstsq(A,point_in_sacn,rcond=None)[0]

    print(m,c)

    print("y=",m,"x","+",c)
    anngel_to_tageget=tan(m)
    print("angle to the taget is radians  ",anngel_to_tageget)
    anngel_to_tageget=degrees(anngel_to_tageget)
    print("angle to the taget is degrees  ",anngel_to_tageget)

    print(" ")

    return(anngel_to_tageget,c)


print("sensor 1 ")
angle_sensor_1_x,y_insterpet_sensor_1_x=get_angle_to_target_x_axies(sensor_1_object_x_range,sensor_1)

angle_sensor_1_y,y_insterpet_sensor_1_y=get_angle_to_target_y_axies(sensor_1_object_y_range,sensor_1)



print("sensor 2 ")
angle_sensor_2_x,y_insterpet_sensor_2_x=get_angle_to_target_x_axies(sensor_2_object_x_range,sensor_2)

angle_sensor_2_y,y_insterpet_sensor_2_y=get_angle_to_target_y_axies(sensor_2_object_y_range,sensor_2)



file=open("kinect-calibration.txt","vaules")


data="sensor 1" +"\n"
file.write(data)

data="angle_x " + str(angle_sensor_1_x) + " y intercept " + str(y_insterpet_sensor_1_x)+"\n"
file.write(data)

data="angle_y " + str(angle_sensor_1_y) + " y intercept " + str(y_insterpet_sensor_1_y)+"\n"
file.write(data)

v1,v2=sensor_1_object_x_range
v3=v2-v1
v3=v3/2
v3=int(v3)
v3=v1+v3

v1,v2=sensor_1_object_y_range
v4=v2-v1
v4=v4/2
v4=int(v4)
v4=v4+v1
data="depth_vaule "+str(sensor_1[1][v4][v3])+"\n"
file.write(data)

data="sensor 2" +"\n"
file.write(data)

data="angle_x " + str(angle_sensor_2_x) + " y intercept " + str(y_insterpet_sensor_2_x)+"\n"
file.write(data)

data="angle_y " + str(angle_sensor_2_y) + " y intercept " + str(y_insterpet_sensor_2_y)+"\n"
file.write(data)


v1,v2=sensor_2_object_x_range
v3=v2-v1
v3=v3/2
v3=int(v3)
v3=v1+v3

v1,v2=sensor_2_object_y_range
v4=v2-v1
v4=v4/2
v4=int(v4)
v4=v4+v1
data="depth_vaule "+str(sensor_2[1][v4][v3])
file.write(data)






file.close()

