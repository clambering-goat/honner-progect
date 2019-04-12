


point_could="point_cloud.xyz"



file=open(point_could,"r")

data=file.readlines()

array=[]
for q in data:
    temp=q.split(" ")
    x=float(temp[0])
    y=float(temp[1])
    z=float(temp[2])

    array.append((x,y,z))



vaule_found=[]
data=[[]]
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



print(data[0])

center_point=0,0

#max x point from center

slice_points = []
for loop1 in data:
    layer_1=loop1
    max_x=[0,0,0]
    min_x=[999999999999999999999999999,0,0]



    for q in layer_1:

        x=q[0]
        y=q[1]
        z=q[2]

        if x > max_x[0]:
            max_x[0]=x
            max_x[1]=y
            max_x[2]=z

        if x< min_x[0]:
            min_x[0]=x
            min_x[1]=y
            min_x[2]=z

    slice_points.append(max_x)
    slice_points.append(min_x)
    print("max fouund ", max_x)
    print("min x found ", min_x)




slice_size=0.4
#bott add in
for q in data[0]:
    x=q[0]
    y=q[1]
    z=q[2]


    if x >min_x[0] and x<max_x[0] and y >min_x[1]-slice_size and y<max_x[1]+slice_size:
        slice_points.append((x,y,z))




#top add in
for q in data[-1]:
    x=q[0]
    y=q[1]
    z=q[2]


    if x >min_x[0] and x<max_x[0] and y >min_x[1]-slice_size and y<max_x[1]+slice_size:
        slice_points.append((x,y,z))



file=open("slice.xyz","vaules")


for w in slice_points:
    data=str(w[0])+" "+str(w[1])+" "+str(w[2])+"\n"
    file.write(data)

file.close()


print("total _points" ,len(layer_1))
print("len of lsice points",len(slice_points))
print("done ")



