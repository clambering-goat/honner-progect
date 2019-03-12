from  graphics import Point,GraphWin
import matplotlib.pyplot as plt







#use the matplotlib  model to make a 2d view of points
class grid_draw_2d :
    def __init__(self,layer="no give name"):
        self.layer=layer
        self.point_list_x=[]
        self.point_list_y=[]
    def add_points(self,x,y):
        self.point_list_x.append(x)
        self.point_list_y.append(y)

    def draw(self,layer="no give name"):

        plt.plot(self.point_list_x, self.point_list_y, 'ro')
        plt.axis([0, 210, 0, 210])
        plt.title(layer)
        plt.show()
        #rest so old point dont show up
        self.point_list_x=[]
        self.point_list_y=[]






def line_to_points(list_of_lines):
    list_of_points={}
    scan_size=0.01
    for layer in list_of_lines:
        list_of_points[layer]=[]
        for line in list_of_lines[layer]:
            start,end,hight=line


            x1,y1=start
            x2,y2=end

            x1=float(x1)
            x2 = float(x2)
            y1 = float(y1)
            y2 = float(y2)

            z1=float(hight)

            #get the diffence between the 2 points

            vaule_x=(x2-x1)
            vaule_y=(y2-y1)




            #add start and end points
            list_of_points[layer].append((x1,y1,z1))
            list_of_points[layer].append((x2,y2,z1))



            #dealt with hozontial line and vertic lines
            if vaule_y==0:

                # y is a constant and x changes

                while x2>x1:
                    x1=x1+scan_size
                    if x2 < x1:
                        break
                    # simple step to nemove negitve numbers
                    if x1 > 0 and y1 > 0:
                        list_of_points[layer].append((x1,y1,z1))

                continue





            if vaule_x==0:

                #x is constant y changes
                while y2>y1:
                    y1=y1+scan_size
                    if y2<y1:
                        break
                    # simple step to nemove negitve numbers
                    if x1 > 0 and y1 > 0:
                        list_of_points[layer].append((x1,y1,z1))
                continue



            m=vaule_y/vaule_x

            c=y1-(m*x1)




            how_far_to_smaple_alone_the_line=0.1

            if x2< x1:
                temp=x1
                x1=x2
                x2=temp

            while x2>x1:
                x1=x1+how_far_to_smaple_alone_the_line
                y=m*x1+c
                if x2 < x1:
                    break
                #simple step to nemove negitve numbers
                if x1 > 0 and y > 0:
                    list_of_points[layer].append((x1,y,z1))



    return(list_of_points)













def g_code_to_lines(file_to_open="no_file"):

    g_code_lines_in_the_g_code={}
    if file_to_open=="no_file":
        print("a file was not given close program")
        exit()

    file = open(file_to_open, "r")
    g_code = file.readlines()

    x_old = -1
    y_old = -1

    current_z_hight=0
    for g_code_lines in  g_code:

        g_code_lines=g_code_lines.strip()

        if g_code_lines[0:7]==";LAYER:":
            current_layer_is=g_code_lines
            g_code_lines_in_the_g_code[g_code_lines]=[]
            print(g_code_lines)



        line_breack=g_code_lines.split(" ")



        if not(line_breack[0]=="G0" or line_breack[0]=="G1"):
            continue


        x_point=-1
        y_point=-1
        #use to remove move commadnt where no filemtn is being deposited

        E_found=False
        for q in line_breack:
            if len(q)<1:
                continue
            if q[0]=="E":
                E_found=True
            if q[0]=="X":
                x_point=q[1:]
            if q[0]=="Y":
                y_point=q[1:]

            if q[0]=="Z":
                current_z_hight=q[1:]


    # to slove the cold start promble and remove the line from 0,0
        if x_old==-1 or y_old==-1:
            x_old = x_point
            y_old = y_point
            continue

        #remove the move comands from g code
        if E_found==False:
           x_old = x_point
           y_old = y_point
           continue


    #here to make skip a line if no x vaule is found
        # here to remove the end line command the switch the print move mode the relitive and move the -20 ,-20

        if float(x_point)<0 or float(y_point)<0:
            continue

        old_x_y_points=(x_old,y_old)
        new_x_y_points=(x_point, y_point)

        g_code_lines_in_the_g_code[current_layer_is].append(((old_x_y_points),(new_x_y_points),current_z_hight))


        x_old=x_point
        y_old=y_point



    return(g_code_lines_in_the_g_code)



rr="box.gcode"

lines=g_code_to_lines(rr)

points=line_to_points(lines)

x_points=[]
y_points=[]
z_points=[]

file=open("point_cloud.xyz","w")


for q in points:
    for w in points[q]:
        x_points.append(w[0])
        y_points.append(w[1])
        z_points.append(w[2])
        data=str(w[0])+" "+str(w[1])+" "+str(w[2])+"\n"

        file.write(data)
    print("layer ", q ," done ")
file.close()
