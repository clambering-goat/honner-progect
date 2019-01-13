

from graphics import *

win = GraphWin(width=200,height=200)

#100 x size and y size 50
pt1 = Point(0,0)
pt2=Point(100,100)
#live draw dunction
line = Line(pt1,pt2)
#updates screen
line.draw(win)

file=open("g_code_one_layer.gcode","r")
line=file.readline()
print(line)




input("press enter to close ")
