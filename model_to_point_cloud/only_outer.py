



file=open("point_cloud.xyz","r")

data=file.readlines()

array=[]
count=0
for q in data:
    count+=1
    temp=q.split(" ")
    x=float(temp[0])
    y=float(temp[1])
    z=float(temp[2])

    array.append((x,y,z))



vaule_found=[]

data=[[0]]
count=0
set_hight=array[0][2]
for q in array:
    if q[2]==set_hight:
        data[count].append(q)
    else:
        data.append([])
        count+=1
        set_hight=q[2]
        data[count].append(q)
        vaule_found.append(q[2])








point_in_range=0.01
for q in data[0]:
    x=q[0]
    y=q[1]
    z=q[2]
    #x move
    for w in data[0]:
        x2=w[0]
        y2=w[1]
        z2=w[2]
        if x2>x and x2<x+point_in_range:






# surfe_points=[]
#
#
# start_point=array[-1]
#

