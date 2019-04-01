


point_could="point_cloud.xyz"



file=open(point_could,"r")

data=file.readlines()

array=[]
for q in data:
    temp=q.split(" ")
    x=float(temp[0])
    y=float(temp[1])
    z=float(temp[2])
    if z>0.2:

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



slice_size=0.1
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



slioet_max_x=0
slioet_max_z=0
siloet_min_x=999999999999999999999999999
siloet_min_z=999999999999999999999999999
for w in slice_points:
    x,y,z=w


    if x>slioet_max_x:
        slioet_max_x=x

    if x<siloet_min_x:
        siloet_min_x=x

    if z>slioet_max_z:
        slioet_max_z=z

    if z< siloet_min_z:
        siloet_min_z=z


box_bond=((siloet_min_x, siloet_min_z), (slioet_max_x, slioet_max_z))

print("box bondersy ",box_bond)

def for_loop_2(v1,v2,step):
    data=[]
    if v1 >v2:
        temp=v2
        v2=v1
        v1=temp

    while(v1<v2):
        data.append(v1)
        v1+=step
    return(data)

#hozontal line
v1=box_bond[0][0]
v2=box_bond[1][0]

hoz_lines=for_loop_2(v1,v2,0.1)

v1=box_bond[0][1]
v2=box_bond[1][1]
verial_line=for_loop_2(v1,v2,0.1)





file=open("slice.xyz","w")




for w in slice_points:
    data=str(w[0])+" "+str(w[1])+" "+str(w[2])+"\n"
    file.write(data)








file.close()




file=open("box.xyz","w")

for w in hoz_lines:
    z=box_bond[0][1]
    x=w
    y=100
    data=str(x)+" "+str(y)+" "+str(z)+"\n"
    file.write(data)

for w in hoz_lines:
    z=box_bond[1][1]
    x=w
    y=100
    data=str(x)+" "+str(y)+" "+str(z)+"\n"
    file.write(data)




for w in verial_line:
    z=w
    x=box_bond[1][0]
    y=100
    data=str(x)+" "+str(y)+" "+str(z)+"\n"
    file.write(data)

for w in verial_line:
    z=w
    x=box_bond[0][0]
    y=100
    data=str(x)+" "+str(y)+" "+str(z)+"\n"
    file.write(data)








file.close()


print("total _points" ,len(layer_1))
print("len of lsice points",len(slice_points))
print("done ")



