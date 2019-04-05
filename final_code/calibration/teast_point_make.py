import numpy as np


object_1=np.zeros((100,100))
object_2=np.zeros((100,100))




for v1 in range(30,80):
    for v2 in range(30,80):

        object_1[v1][v2]=100


for v1 in range(30,80):
    count = 100
    for v2 in range(30,80):
        count+=1
        object_2[v1][v2]=count

count = 100
for v1 in range(30,80):
    count -= 1
    for v2 in range(30,80):

        object_2[v1][v2]=count



np.save("dobject _1",object_1)
np.save("dobject _2",object_2)