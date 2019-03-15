


import matplotlib.pyplot as plt



points=[]

size_grid=9

for x in range(size_grid):
    for y in range(size_grid):
        points.append((x,y))




amount_to_move=2

free_points=[]





for p1 in points:
    x_p_teast = True
    x_n_teast=True
    y_p_teast = True
    y_n_teast = True

    x1=p1[0]
    y1=p1[1]

    #move x
    x_move_p=x1+amount_to_move

    x_move_n=x1-amount_to_move

    #move y

    y_move_p=y1+amount_to_move

    y_move_n=y1-amount_to_move


    print("looking at point",x1,y1)


    for p2 in points:
        x2=p2[0]
        y2=p2[1]

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
        free_points.append((x1,y1))

    if x_n_teast==True:
        free_points.append((x1,y1))

    if y_p_teast==True:
        free_points.append((x1, y1))

    if y_n_teast==True:
        free_points.append((x1, y1))

point_list_x=[]
point_list_y=[]
for q in free_points:
    point_list_x.append(q[0])
    point_list_y.append(q[1])

plt.plot(point_list_x,point_list_y, 'ro')



plt.axis([-10, 10, -10, 10])
plt.title("map")
plt.show()





