
point_could="trangle_up.xyz"



file=open(point_could,"r")

data=file.readlines()

array=[]


for q in data:
    temp=q.split(" ")
    x=float(temp[0])
    y=float(temp[1])
    z=float(temp[2])
    #removes the basic points assmenting the layer hieght is 0.2
    if z>1.2:

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







#max x point from center

file=open("x_max_min.txt","w")

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
    data=str(max_x[0])+" "+str(min_x[0])+" "+str(z)+"\n"
    file.write(data)
file.close()