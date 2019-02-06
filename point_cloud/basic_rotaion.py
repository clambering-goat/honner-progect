
import matplotlib.pyplot as plt
from math import sin,cos,radians
base_points=[]

z_points=20
for x_point in range(2):
    for y_point in range(2):
        base_points.append((x_point*2,y_point*2,z_points*2))







# rotaion points
angle=120
angle=radians(angle)
s=sin(angle)
c=cos(angle)

print(s)
print(c)
new_points_to_add=[]
for loop in base_points:
    x=loop[0]
    y=loop[1]
    z=loop[2]
    #math from roation
    x1=(x*c)-(y*s)
    y1=(x*s)+(y*c)

    new_points_to_add.append((x1,y1,z))










print("distance of points ")
y_count=-1
x_count=-1
for w in new_points_to_add:
    y_count=y_count+1
    x_count=-1
    for q in new_points_to_add:
        x_count=x_count+1
        a=q[0]-w[0]
        b=q[1]-w[1]

        c = a ** 2 + b ** 2
        c=c**0.5

        a=base_points[x_count][0]-base_points[y_count][0]
        b=base_points[x_count][1]-base_points[y_count][1]
        c2 = (a ** 2) + (b ** 2)
        c2=(c2**0.5)

        print("start ",c2," end ",c," ",x_count,y_count)




x_list=[]
y_list=[]
z_list=[]
for q in base_points:

    x_list.append(q[0])
    y_list.append(q[1])
    z_list.append(q[2])




for q in new_points_to_add:

    x_list.append(q[0])
    y_list.append(q[1])
    z_list.append(q[2])





plt.plot(x_list, y_list, 'bo')




plt.axis([-20, 20, -20, 20])
plt.show()
