
import time
from graphics import *

win = GraphWin(width=200,height=200)



file=open("bar teast.gcode","r")


g_code=file.readlines()


x_old=-1
y_old=-1


array_of_points=[]




def line_equation(x1,y1,x2,y2):

    m=(y2-y1)/(x2-x1)

    c=y1-(m*x1)


    x_leanth=(y2-y1)
    y_leanth=(x2-x1)

    leanth_of_line=0.5**(x_leanth**2+y_leanth**2)
    print("line leanth",leanth_of_line)

    moving_factor=0.1

    array_of_points




    #y=mx+c




for g_code_lines in  g_code:

    g_code_lines=g_code_lines.strip()

    if g_code_lines[0:7]==";LAYER:":
        print(g_code_lines)



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


    pt1 = Point(x_old,y_old)
    pt2=Point(x_point,y_point)


    y_leanth=(float(y_old)-float(y_point))
    x_leanth=(float(x_old)-float(x_point))

    leanth_of_line=(x_leanth**2+y_leanth**2)**0.5

    if leanth_of_line>0:
        array_of_points.append(leanth_of_line)



    line = Line(pt1,pt2)

    x_old=x_point
    y_old=y_point



    if x_old==0:
        print("?")
    #updates screen
    line.draw(win)
    #time.sleep(0.01)
print("done")
print(min(array_of_points))
input("press enter to close ")
