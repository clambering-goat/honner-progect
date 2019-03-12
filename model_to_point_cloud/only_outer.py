



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



while True:



    for q in data[0]:


        print(q)





# surfe_points=[]
#
#
# start_point=array[-1]
#

