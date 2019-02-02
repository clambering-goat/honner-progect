def line_equation(x1,y1,x2,y2):

    list_of_points=[]
    x1=float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)


    vaule_x=(x2-x1)
    vaule_y=(y2-y1)

    leanth_of_line=0.5**(vaule_x**2+vaule_y**2)

    print("line leanth",leanth_of_line)

    #add start and end points
    list_of_points.append((x1,y1))
    list_of_points.append((x2,y2))

    #get the diffence between the 2 points
    vaule_x=(x2-x1)
    vaule_y=(y2-y1)


    #dealt with hozontial line and vertic lines
    if vaule_y==0:
        print("vertiacal line")
        # y is a constant and x changes
        #round down
        scan1=int(x1)
        #round up
        scan2=round(x2)
        for x in range(scan1,scan2):
            list_of_points.append((x,y1))


        return(list_of_points)


    if vaule_x==0:
        print(" horzontiale line")
        #x is constant y changes
        #round down
        scan1=int(y1)
        #round up
        scan2=round(y2)
        for y in range(scan1,scan2):
            list_of_points.append((x1,y))


        return(list_of_points)





    m=vaule_y/vaule_x

    c=y1-(m*x1)






    #to add scan in x xies
    #use start point of line as start and end as end


    #round down
    scan1=int(x1)
    #round up
    scan2=round(x2)

    print("x scan")

    if scan2< scan1:
        temp=scan1
        scan1=scan2
        scan2=temp

    for x in range(scan1,scan2):

        y=m*x+c
        x=float(x)
        list_of_points.append((x,y))
        print()

    return(list_of_points)
#redundent code
'''
    #round down
    scan1=int(y1)
    #round up
    scan2=round(y2)

    print("y scan")
    for y in range(scan1,scan2):
        x=(y-c)/m
        print(x,y)
        print()



for x1 in range(-10,10):
    for y1 in range(-10,10):
        for x2 in range(-10,10):
            for y2 in range(-10,10):

'''
x1,y1=0,0
x2,y2=5,5
points=line_equation(x1,y1,x2,y2)
for q in points:
    print(q)
