
import time
from graphics import *

win = GraphWin(width=200,height=200)



#file=open("bar teast.gcode","r")


#file=open("gear.gcode","r")
file=open("gear2.gcode","r")

g_code=file.readlines()


x_old=-1
y_old=-1




list_of_points = []


def line_equation(x1,y1,x2,y2):

    x1=float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)


    vaule_x=(x2-x1)
    vaule_y=(y2-y1)

    leanth_of_line=0.5**(vaule_x**2+vaule_y**2)


    #add start and end points
    list_of_points.append((x1,y1))
    list_of_points.append((x2,y2))

    #get the diffence between the 2 points
    vaule_x=(x2-x1)
    vaule_y=(y2-y1)


    #dealt with hozontial line and vertic lines
    if vaule_y==0:

        # y is a constant and x changes
        #round down
        scan1=int(x1)
        #round up
        scan2=round(x2)
        for x in range(scan1,scan2):
            list_of_points.append((x,y1))


        return


    if vaule_x==0:

        #x is constant y changes
        #round down
        scan1=int(y1)
        #round up
        scan2=round(y2)
        for y in range(scan1,scan2):
            list_of_points.append((x1,y))


        return





    m=vaule_y/vaule_x

    c=y1-(m*x1)






    #to add scan in x xies
    #use start point of line as start and end as end


    #round down
    scan1=int(x1)
    #round up
    scan2=round(x2)


    if scan2< scan1:
        temp=scan1
        scan1=scan2
        scan2=temp

    for x in range(scan1,scan2):

        y=m*x+c
        x=float(x)
        list_of_points.append((x,y))


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
    for q in line_breack:
        if len(q)<1:
            continue
        if q[0]=="X":
            x_point=q[1:]
        if q[0]=="Y":
            y_point=q[1:]


# to slove the cold start promble and remove the line from 0,0
    if x_old==-1 or y_old==-1:
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
for q in list_of_points:

    pix=Point(q[0],q[1])
    pix.draw(win)
    #print(q)
    #time.sleep(0.1)
print("done")


