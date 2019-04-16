from math import sin, cos, radians


def file_to_array(file_name):
    file = open(file_name, "r")

    data = file.readlines()

    array = []

    for q in data:
        temp = q.split(" ")
        x = float(temp[0])
        y = float(temp[1])
        z = float(temp[2])

        # removes the basic points assmenting the layer hieght is 0.2
        if z > 0.2:
            array.append((x, y, z))

    return array


def split_into_layers(in_array):
    out_array = [[]]

    layer_number = 0

    # line 1 z vaule from file
    curretn_hight = in_array[0][2]

    for vaules in in_array:
        if vaules[2] == curretn_hight:
            out_array[layer_number].append(vaules)
        else:
            out_array.append([])
            layer_number += 1

            curretn_hight = vaules[2]

            out_array[layer_number].append(vaules)

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


def roation(array_in, angle):
    angle = radians(angle)
    s = sin(angle)
    c = cos(angle)

    out_array = []
    layer_number = -1

    for layer in array_in:
        out_array.append([])
        layer_number += 1
        center_point = find_center_point(layer)
        for vailes in layer:
            x, y, z = vailes

            x = x - center_point[0]
            y = y - center_point[1]

            x1 = (x * c) - (y * s)
            y1 = (x * s) + (y * c)

            x1 = x1 + center_point[0]
            y1 = y1 + center_point[1]


            out_array[layer_number].append((x1, y1, z))

    return out_array


def make_siltot(in_array,angle):
    slice_points = []


    angle = radians(-angle)
    s = sin(angle)
    c = cos(angle)

    for layer in in_array:
        center_point = find_center_point(layer)
        max_x = [-9999999999999999, 0, 0]
        min_x = [999999999999999999999999999, 0, 0]

        for vaules in layer:

            x = vaules[0]
            y = vaules[1]
            z = vaules[2]

            if x > max_x[0] and y> center_point[1]-0.01 and y< center_point[1]+0.01 :
                x = x - center_point[0]
                y = y - center_point[1]

                x = (x * c) - (y * s)
                y = (x * s) + (y * c)

                x = x + center_point[0]
                y = y + center_point[1]

                max_x[0] = x
                max_x[1] = y
                max_x[2] = z

            if x < min_x[0]and  y> center_point[1]-0.01 and y< center_point[1]+0.01 :
                x = x - center_point[0]
                y = y - center_point[1]

                x = (x * c) - (y * s)
                y = (x * s) + (y * c)

                x = x + center_point[0]
                y = y + center_point[1]

                min_x[0] = x
                min_x[1] = y
                min_x[2] = z

        slice_points.append(max_x)
        slice_points.append(min_x)

    # slice_size = 0.1
    # # bott add in
    #
    # for vaules in in_array[0]:
    #     x = vaules[0]
    #     y = vaules[1]
    #     z = vaules[2]
    #
    #     if x > min_x_mm[0] and x < max_x_mm[0] and y > min_x_mm[1] - slice_size and y < max_x_mm[1] + slice_size:
    #         slice_points.append((x, y, z))
    #
    # # top add in
    # for vaules in in_array[-1]:
    #     x = vaules[0]
    #     y = vaules[1]
    #     z = vaules[2]
    #
    #     if x > min_x_mm[0] and x < max_x_mm[0] and y > min_x_mm[1] - slice_size and y < max_x_mm[1] + slice_size:
    #         slice_points.append((x, y, z))

    return slice_points




array_1 = file_to_array("point_cloud.xyz")

array_2 = split_into_layers(array_1)



file=open("siloet.xyz ","w")


angle=50
print("working on angle ", angle)
array_3 = roation(array_2,angle)

array_4=make_siltot(array_3,angle)




for vaules in array_4:
    data = str(vaules[0]) + " " + str(vaules[1]) + " " + str(vaules[2]) + "\n"
    # print(data)
    file.write(data)



file.close()



file_2 = open("point_coulder_rotared.xyz", "w")

for layer in array_3:
    for vaules in layer:
        data = str(vaules[0]) + " " + str(vaules[1]) + " " + str(vaules[2]) + "\n"
        # print(data)
        file_2.write(data)


file_2.close()
