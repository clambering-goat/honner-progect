





from math import sin,cos,radians
import numpy as np
import os

def split_into_layers(in_array):
    out_array = [[]]

    layer_number = 0

    # line 1 z vaule from file
    curretn_hight = in_array[0][2]

    for vaules in in_array:
        vaules_split=vaules.split(" ")
        if vaules_split[2] == curretn_hight:

            x = float(vaules_split[0])
            y = float(vaules_split[1])
            z = float(vaules_split[2])
            out_array[layer_number].append((x,y,z))
        else:
            out_array.append([])
            layer_number += 1

            curretn_hight = vaules_split[2]

            x = float(vaules_split[0])
            y = float(vaules_split[1])
            z = float(vaules_split[2])
            out_array[layer_number].append((x, y, z))

    return out_array


def find_center_point(layer_in):
    max_x = -9999999999
    min_x = 9999999999

    max_y = -9999999999
    min_y = 9999999999

    for vaule in layer_in:
        x, y, z = vaule


        if x > max_x:
            max_x = x

        if x < min_x:
            min_x = x

        if y > max_y:
            max_y = y

        if y < min_y:
            min_y = y

    center_x = min_x + (max_x - min_x) / 2
    center_y = min_y + (max_y - min_y) / 2
    center = center_x, center_y
    return center


def roatation(angle, rotation_axies, point_could,file_out):
    layerss=split_into_layers(point_could)
    angle = radians(angle)

    s = sin(angle)
    c = cos(angle)


    for layer in layerss:
        center_point = find_center_point(layer)





        for points in layer:

            x, y, z = points



            x = x - center_point[0]
            y = y - center_point[1]



            #y roaion
            if rotation_axies == "y":
                z1 = (x * s) + (z * c)
                y1 = y
                x1 = (x * c) - (z * s)

            if rotation_axies == "x":
                x1 = x
                y1 = (z * s) + (y * c)
                z1 = (z * c) - (y * s)



            if rotation_axies == "z":
                x1 = (x * c) - (y * s)
                y1 =  (x * s) + (y * c)
                z1 = z



            x1 = x1 + center_point[0]
            y1 = y1 + center_point[1]

            data = str(x1) + " " + str(y1) + " " + str(z1) + "\n"
            file_out.write(data)


