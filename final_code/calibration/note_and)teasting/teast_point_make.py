import numpy as np


object_1=np.zeros((100,100))
object_2=np.zeros((100,100))




for v1 in range(30,80):
    for v2 in range(30,80):

        object_1[v1][v2]=100


# for v1 in range(30,80):
#     count = 100
#     for v2 in range(30,80):
#         count+=1
#         object_2[v1][v2]=count

count = 100
for v1 in range(30,80):
    count -= 0.1
    for v2 in range(30,80):

        object_2[v1][v2]=count



file_name="object _1.xyz"

file = open(file_name, "w")

x_p=-1
y_p=-1
for y in object_1:
    y_p+=1
    x_p=-1
    for z_data in y:
        x_p+=1
        transpotion=z_data
        data=str(x_p)+" "+str(y_p)+" "+str(transpotion)+" \n"
        file.write(data)
file.close()






file_name="object _2.xyz"

file = open(file_name, "w")

x_p=-1
y_p=-1
for y in object_2:
    y_p+=1
    x_p=-1
    for z_data in y:
        x_p+=1
        transpotion=z_data
        data=str(x_p)+" "+str(y_p)+" "+str(transpotion)+" \n"
        file.write(data)
file.close()






np.save("dobject _1",object_1)
np.save("dobject _2",object_2)