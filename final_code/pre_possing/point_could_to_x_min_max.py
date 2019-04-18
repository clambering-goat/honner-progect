
















class get_x_min_to_x_max():
    def __init__(self, file_to_open):

        self.x_center=105
        #file_to_open= "thin_wall.xyz"



        file=open(file_to_open, "r")

        data=file.readlines()

        array=[]


        for q in data:
            temp=q.split(" ")
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


        for q in array:
            if q[2]==set_hight:
                data[count].append(q)
            else:
                data.append([])
                count+=1
                set_hight=q[2]
                data[count].append(q)
                vaule_found.append(q[2])







        #max x point from center
        self.file_out_name="x_max_min"+file_to_open[0:-4]+".txt"

        file=open(self.file_out_name,"w")

        for loop1 in data:
            layer_1=loop1
            max_x=[0,999999999999999999999999999,0]
            min_x=[999999999999999999999999999,999999999999999999999999999,0]


            #find the x points
            max_x_points=[]
            min_x_proints=[]
            y_center_vaule=999999999
            y_center_points=[]
            for q in layer_1:

                if q[0] >= max_x[0]:

                    max_x[0]=q[0]

                if q[0]<= min_x[0]:

                    min_x[0]=q[0]

                costance_z=q[2]

                if q[0]>self.x_center-0.2and q[0]<self.x_center+0.2:
                    y_center_points.append(q[1])

            for q in layer_1:
                if q[0]>=max_x[0]:
                    max_x_points.append(q)

                if q[0]<= min_x[0]:
                    min_x_proints.append(q)


            for q in y_center_points:
                if q<y_center_vaule:
                    y_center_vaule=q


            #find the max y in max x poitns
            for q in max_x_points:
                if q[1] <= max_x[1]:
                    max_x[1] = q[1]

            for q in min_x_proints:
                if q[1] <= min_x[1]:
                    min_x[1] = q[1]

            #124.8
            #76.339

            #85.2
            #75.2

            #134.8
            #6.9
            #124.8 125.2
            # 85.2 75.2
            # 134.8 3.3

            data=str(max_x[0])+" "+str(max_x[1])+" "+str(min_x[0])+" "+str(min_x[1])+" "+str(self.x_center)+" "+str(y_center_vaule)+" "+str(costance_z)+"\n"
            file.write(data)
        file.close()

    def get_file_name(self):
        return self.file_out_name