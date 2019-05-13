
def get_points(file_to_open):
    import math
    x_center=105
    #file_to_open= "point_cloud_of_changin_in_depth_teast.xyz"



    file=open(file_to_open, "r")

    data=file.readlines()

    array=[]


    for point in data:
        temp=point.split(" ")
        x=float(temp[0])
        y=float(temp[1])
        z=float(temp[2])

        #removes the basic points assmenting the layer hieght is 0.2
        if z>1.2:

            array.append((x,y,z))



    vaule_found=[]
    data=[[]]
    count=0

    set_hight=array[0][2]


    for point in array:
        if point[2]==set_hight:
            data[count].append(point)
        else:
            data.append([])
            count+=1
            set_hight=point[2]
            data[count].append(point)
            vaule_found.append(point[2])







    #max x point from center
    file_out_name="chane_y_over_x_"+file_to_open[0:-4]+"_.txt"

    file=open(file_out_name,"w")
    count=0
    for layer in data:
        count+=1
        print(" get point for layer ",layer[0][2])
        higth=layer[0][2]
        max_x=0
        min_x=999999999999999999999999999


        #find the  max x points

        for point in layer:

            if point[0] >= max_x:

                max_x=point[0]

            if point[0]<= min_x:

                min_x=point[0]


        outer_points=[]
        min_x=int(min_x)

        max_x=math.ceil(max_x)
        max_x=int(max_x)
        error_margion=0.05
        for counter in range(min_x,max_x):
            y_min = 9999
            x_point_looking=counter
            for point in layer:
                if x_point_looking>point[0]-error_margion and x_point_looking<point[0]+error_margion:
                    if point[1]<=y_min:
                        y_min=point[1]

            if y_min !=9999:
                data_o=str(x_point_looking)+" "+str(y_min)+" "+str(higth)+"\n"

                file.write(data_o)


    file.close()

    return file_out_name

