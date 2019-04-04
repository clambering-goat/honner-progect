
import time
from graphics import *

#win = GraphWin(width=200,height=200)



#file=open("bar teast.gcode","r")


file=open("gear.gcode","r")
#file=open("gear2.gcode","r")

g_code=file.readlines()


x_old=-1
y_old=-1




list_of_points = []


def line_equation(x1,y1,x2,y2):

    x1=float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)

    scan_size=0.01
    START_POINTS_1=x1,y1
    ENDPOINTS_1=x2,y2
    #get the diffence between the 2 points

    vaule_x=(x2-x1)
    vaule_y=(y2-y1)

    leanth_of_line=0.5**(vaule_x**2+vaule_y**2)


    #add start and end points
    list_of_points.append((x1,y1))
    list_of_points.append((x2,y2))



    #dealt with hozontial line and vertic lines
    if vaule_y==0:

        # y is a constant and x changes

        while x2>x1:
            x1=x1+scan_size
            if x2 < x1:
                break
            # simple step to nemove negitve numbers
            if x1 > 0 and y1 > 0:

                list_of_points.append((x1,y1))


        return


    if vaule_x==0:

        #x is constant y changes
        while y2>y1:
            y1=y1+scan_size
            if y2<y1:
                break
            # simple step to nemove negitve numbers
            if x1 > 0 and y1 > 0:

                list_of_points.append((x1,y1))


        return





    m=vaule_y/vaule_x

    c=y1-(m*x1)






    #to add scan in x xies
    #use start point of line as start and end as end


    # scan need to be with in the points







    if x2< x1:
        temp=x1
        x1=x2
        x2=temp

    while x2>x1:
        x1=x1+scan_size
        y=m*x1+c
        if x2 < x1:
            break
        #simple step to nemove negitve numbers
        if x1 > 0 and y > 0:
            list_of_points.append((x1,y))
            if y > 130:
                print("?")


    return






for g_code_lines in  g_code:

    g_code_lines=g_code_lines.strip()

    if g_code_lines[0:7]==";LAYER:":
        print(g_code_lines)

    if g_code_lines[0:8] == ";LAYER:1":
        break

    line_breack=g_code_lines.split(" ")



    if not(line_breack[0]=="G0" or line_breack[0]=="G1"):
        continue


    x_point=-1
    y_point=-1
    #use to remove move commadnt where to filemtn is being deposited
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




    line_equation(x_old, y_old, x_point, y_point)





    x_old=x_point
    y_old=y_point


# random point aperar need to make code to look for ups in point clould
#need to remove tranion of print head from g code
print("drawing point cloud ")


#grouping function


'''
group=[]
count=-1

scan_size=10
while len(list_of_points)>0:
    count = count + 1
    x, y = list_of_points[0]

    bond_max_x = x + scan_size
    bond_max_y = y + scan_size

    bond_min_x = x - scan_size
    bond_min_y = y - scan_size
    group.append([])
    print(len(list_of_points))
    list_of_point_to_remove=[]
    for q in list_of_points:
        x,y=q

        if x<0 or y<0:
            print("? help ")
            print(x,y)
            exit()

        if x>bond_min_x and x<bond_max_x and y>bond_min_y and y<bond_max_y:
            group[count].append((x,y))
            list_of_point_to_remove.append((x,y))
    for q in list_of_point_to_remove:
        list_of_points.remove(q)
print(len(group)," groups where found with a prosimity of ",scan_size)

'''
'''
import matplotlib.pyplot as plt
x_list=[]
y_list=[]
for q in list_of_points:

    x_list.append(q[0])
    y_list.append(q[1])
plt.plot(x_list, y_list, 'ro')
plt.axis([50, 200, 50, 200])
plt.show()


'''




file = open("point_cloud_out_old_working.xyz", "w")
for q in list_of_points:

    data = str(q[0]) + " " + str(q[1])+ " 0 ""\n"
    file.write(data)
    #pix=Point(q[0],q[1])
    #pix.draw(win)
    #print(q)
    #time.sleep(0.1)
file.close()
input("press to close")
print("done")
