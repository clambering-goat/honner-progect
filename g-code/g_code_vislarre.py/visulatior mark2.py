
import time
from graphics import *

win = GraphWin(width=200,height=200)



file=open("bar teast.gcode","r")


g_code=file.readlines()


x_old=0
y_old=0

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
    #time.sleep(0.01)
print("done")

input("press enter to close ")
