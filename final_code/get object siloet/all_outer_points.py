
from math import sin,cos,radians
def rotatin_points(array,angle):

    angle=radians(angle)
    s=sin(angle)
    c=cos(angle)
    ration_array = []
    for loop in array:
        x = loop[0]
        y = loop[1]
        z = loop[2]
        # math from roation
        x1 = (x * c) - (y * s)
        y1 = (x * s) + (y * c)

        ration_array.append((x1, y1, z))
    return ration_array



def find_center(layer):

    max_x=0
    min_x=999999999999999999
    max_y=0
    min_Y=999999999999999999
    for q in layer:
        x,y,z=q

        if x > max_x[0]:
            max_x[0] = x


        if x < min_x[0]:
            min_x[0] = x


        if y > max_y[0]:
            max_y[0] = y


        if y < min_Y[0]:
            min_Y[0] = x

    center_x=min_x+(max_x-min_x)/2
    center_y=min_Y+(max_y-min_Y)/2
    center=center_x,center_y
    return center

def get_siloet(array):
    vaule_found = []
    data = [[]]
    count = 0

    set_hight = array[0][2]

    for q in array:
        if q[2] == set_hight:
            data[count].append(q)
        else:
            data.append([])
            count += 1
            set_hight = q[2]
            data[count].append(q)
            vaule_found.append(q[2])




    center_point = 0, 0

    # max x point from center

    slice_points = []

    for loop1 in data:
        layer_1 = loop1
        max_x = [0, 0, 0]
        min_x = [999999999999999999999999999, 0, 0]

        for q in layer_1:

            x = q[0]
            y = q[1]
            z = q[2]

            if x > max_x[0]:
                max_x[0] = x
                max_x[1] = y
                max_x[2] = z

            if x < min_x[0]:
                min_x[0] = x
                min_x[1] = y
                min_x[2] = z

        slice_points.append(max_x)
        slice_points.append(min_x)

    slice_size = 0.1
    # bott add in
    for q in data[0]:
        x = q[0]
        y = q[1]
        z = q[2]

        if x > min_x[0] and x < max_x[0] and y > min_x[1] - slice_size and y < max_x[1] + slice_size:
            slice_points.append((x, y, z))

    # top add in
    for q in data[-1]:
        x = q[0]
        y = q[1]
        z = q[2]

        if x > min_x[0] and x < max_x[0] and y > min_x[1] - slice_size and y < max_x[1] + slice_size:
            slice_points.append((x, y, z))

    return slice_points






point_could="point_cloud.xyz"


file=open(point_could,"r")

data=file.readlines()

array=[]

for q in data:
    temp=q.split(" ")
    x=float(temp[0])
    y=float(temp[1])
    z=float(temp[2])
    #removes the basic points assmenting the layer hieght is 0.2
    if z>0.2:

        array.append((x,y,z))

#get center



file=open("slice.xyz","w")

for angle in range(0,90,10):

    array_r=rotatin_points(array,angle)
    file_2 = open("point_coulder_rotared"+str(angle)+".xyz", "w")
    for w in array_r:
        data=str(w[0])+" "+str(w[1])+" "+str(w[2])+"\n"
        #print(data)
        file_2.write(data)




    silot=get_siloet(array_r)

    for w in silot:
        data=str(w[0])+" "+str(w[1])+" "+str(w[2])+"\n"
        #print(data)
        file_2.write(data)

file.close()




