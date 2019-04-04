
import matplotlib.pyplot as plt


file=open("point_cloud.xyz","r")

data=file.readlines()

array=[]
count=0
for q in data:
    count+=1
    temp=q.split(" ")
    x=float(temp[0])
    y=float(temp[1])
    z=float(temp[2])

    array.append((x,y,z))



vaule_found=[]

data=[[0]]
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




for yyy in range(150,200,10):


    amount_to_move=yyy/100

    free_points=[]





    for p1 in data[2]:


        x_p_teast = True
        x_n_teast=True
        y_p_teast = True
        y_n_teast = True
        z_p_teast=True
        x1=p1[0]
        y1=p1[1]
        z1=p1[2]

        #move x
        x_move_p=x1+amount_to_move

        x_move_n=x1-amount_to_move

        #move y

        y_move_p=y1+amount_to_move

        y_move_n=y1-amount_to_move




        for p2 in data[2]:


            x2=p2[0]
            y2=p2[1]
            z2=p2[2]
            if x1==x2 and y1==y2:
                continue


            if   x2>x1   and x2<x_move_p:
                x_p_teast=False


            if   x2>x_move_n   and x2<x1:
                x_n_teast=False

            if y2>y1 and y2<y_move_p:
                y_p_teast=False

            if y2>y_move_n and y2<y1:
                y_n_teast=False


        if x_p_teast==True:
            free_points.append((x1,y1,z1))

        if x_n_teast==True:
            free_points.append((x1,y1,z1))

        if y_p_teast==True:
            free_points.append((x1,y1,z1))

        if y_n_teast==True:
            free_points.append((x1,y1,z1))







    file=open("surface_points"+str(yyy)+".xyz","w")

    for q in free_points:

        x=str(q[0])
        y=str(q[1])
        z=str(q[2])

        data_out=x+" "+y+" "+z+"\n"
        file.write(data_out)

    file.close()



# surfe_points=[]
#
#
# start_point=array[-1]
#

