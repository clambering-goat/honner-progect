
import time
from graphics import *

win = GraphWin(width=200,height=200)



file=open("g_code_one_layer.gcode","r")


g_code_lines=file.readlines()


x_old=0
y_old=0

for points in g_code_lines:

    points=points.strip()
    line_breack=points.split(" ")

    x_point=-1
    y_point=-1
    for q in line_breack:
        if q[0]=="X":
            x_point=q[1:]
        if q[0]=="Y":
            y_point=q[1:]

    if x_point==-1 or y_point==-1:
        continue


    pt1 = Point(x_old,y_old)
    pt2=Point(x_point,y_point)

    line = Line(pt1,pt2)

    x_old=x_point
    y_old=y_point



    if x_old==0:
        print("?")
    #updates screen
    line.draw(win)
    time.sleep(0.01)
print("done")

input("press enter to close ")
