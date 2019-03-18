
#based on the papaer
#https://www.arcjournals.org/pdfs/ijcrce/v2-i3/2.pdf


#only work in 2d to start with

#teasting
#demo point cloud


import numpy as np









def Euclidean_distance(p1,p2):

    x1=p1[0]
    y1=p1[1]


    x2=p2[0]
    y2=p2[1]



    v1=x1-x2
    v2=y1-y2

    c=v1**2+v2**2

    c=c**0.5

    return (c)



def part1_find_neighbors(K,point_could):

    distance_to_all_points=[]
    point_distace_map={}
    points_and_neighbors_and_v_vaule={}
    for p1 in point_could:
        points_and_neighbors_and_v_vaule[p1]=[[], []]

        close_points=np.full((K,3),np.inf)



        for p2 in point_could:

            distace=Euclidean_distance(p2,p1)


            for count  in range(K):
                d=close_points[count][0]
                if  distace <d:
                    close_points[count][0]=distace
                    close_points[count][1]=p2[0]
                    close_points[count][2]= p2[1]
                    break





        for adding_vauler in close_points:
            x=adding_vauler[1]
            y=adding_vauler[2]
            points_and_neighbors_and_v_vaule[p1][0].append((x,y))

    return(points_and_neighbors_and_v_vaule)



def part2_R_and_V(points_and_neighbors_and_v_vaule):

    vx_max=0
    vx_min=99999999999999999999999999

    vy_max=0
    vy_min=9999999999999999999999999
    for point in points_and_neighbors_and_v_vaule:

        x1=point[0]
        y1=point[1]

        neighbors=points_and_neighbors_and_v_vaule[point][0]
        k=len(neighbors)

        vx=0
        vy=0
        for p2 in neighbors:
            x2=p2[0]
            y2=p2[1]

            vx=vx+(x2-x1)
            vy=vy+(y2-y1)


        factor=1/(k-1)

        vx=vx*factor
        vy=vy*factor
        points_and_neighbors_and_v_vaule[point][1].append((vx,vy))


        if vx>vx_max:
            vx_max=vx

        if vx<vx_min:
            vx_min=vx

        if vy>vy_max:
            vy_max=vy

        if vy<vy_min:
            vy_min=vy


    Rx=vx_max-vx_min
    Ry=vy_max-vy_min

    return(Rx,Ry,points_and_neighbors_and_v_vaule)



def part3_find_edge(Rx,Ry,movidfer,points_and_neighbors_and_v_vaule):
    edge_point=[]



    for point_1 in  points_and_neighbors_and_v_vaule:
        V_vaules=points_and_neighbors_and_v_vaule[point_1][1]

        k=len(points_and_neighbors_and_v_vaule[point_1][0])
        c=k+movidfer
        Vx=V_vaules[0][0]
        Vy=V_vaules[0][1]

        if abs(Vx)>abs(Rx)/c:
            edge_point.append(point_1)

        if abs(Vy)>abs(Ry)/c:
            edge_point.append(point_1)

    return(edge_point)


point_could = []
for x in range(100):
    for y in range(100):
        point_could.append((x, y))



K=5
c_movidfer=15
c = K + c_movidfer

#K=11
#c_movidfer=10






point_closees_nabors=part1_find_neighbors(K,point_could)


Rx,Ry,points_and_neighbors_and_v_vaule=part2_R_and_V(point_closees_nabors)



edge_points=part3_find_edge(Rx,Ry,c_movidfer,points_and_neighbors_and_v_vaule)


#if len(edge_points)<1:
#    print("vaule bad no edge found ")


if len(edge_points)>1 and (len(point_could)*len(point_could[0])) != len(edge_points):
    print("good vaule ",K,c_movidfer)



    file = open("edge points k vaule "+str(K)+"c vaule "+str(c_movidfer)+".xyz", "w")


    for q in edge_points:
        x = str(q[0])
        y = str(q[1])

        data_out = x + " " + y +"\n"
        file.write(data_out)

    file.close()
