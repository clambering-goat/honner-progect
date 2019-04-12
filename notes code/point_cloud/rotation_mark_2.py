

from math import sin,cos,radians
base_points=[]





z_points=20
for x_point in range(0,6):
    for y_point in range(0,6):
        base_points.append((10+x_point*2,10+y_point*2,y_point+z_points*2))







# rotaion points
new_points_to_add=[]
for loop1 in range(0,360,90):
    angle=loop1
    angle=radians(angle)
    s=sin(angle)
    c=cos(angle)

    print(s)
    print(c)

    for loop in base_points:
        x=loop[0]
        y=loop[1]
        z=loop[2]
        #math from roation
        x1=(x*c)-(y*s)
        y1=(x*s)+(y*c)

        new_points_to_add.append((x1,y1,z))


#
# for loop1 in range(0,360,10):
#     angle=loop1
#     angle=radians(angle)
#     s=sin(angle)
#     c=cos(angle)
#
#     print(s)
#     print(c)
#
#     for loop in base_points:
#         x=loop[0]
#         y=loop[1]
#         z=loop[2]
#         #math from roation
#         x1=(x*c)-(y*s)
#         y1=(x*s)+(y*c)
#
#         new_points_to_add.append((x1,y1,z))
#






file=open("360_rotaion.xyz","vaules")
for q in base_points:
    data=str(q[0])+" "+str(q[1])+" "+str(q[2])+"\n"
    file.write(data)




for q in new_points_to_add:
    data=str(q[0])+" "+str(q[1])+" "+str(q[2])+"\n"
    file.write(data)

file.close()

