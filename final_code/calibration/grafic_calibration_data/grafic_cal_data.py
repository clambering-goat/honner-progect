


import os
from matplotlib import pyplot

#grafic disatance change
dir_to_look="./"

distance_store=[]
distance_array=[]
distance=0
file_list=[]
for files in os.listdir(dir_to_look):
    if files[-4:len(files)]==".txt":
        file_list.append(files)


sotred_file_list=[]
for q in range(10,200,10):
    for w in file_list:
        split_1=w.split("+")
        split_2=split_1[-1]
        vaule=int(split_2[0:-4])

        if vaule==q:
            sotred_file_list.append(w)
            break

for files in sotred_file_list:
    print(q)


    file=open(files,"r")
    data=file.readlines()
    distance+=10
    distance_array.append(distance)
    for q in data:
        key_vaule=q.split(" ")
        data_2 =key_vaule[1:]#.strip()
        key_vaule=key_vaule[0]

        if key_vaule=="center_is":
            data_2=data_2[1].strip()
            data_2=data_2[0:-1]

            data_2=float(data_2)
            distance_store.append(data_2)



old=distance_store[0]
for q in distance_store[1:]:
    print(q-old)
    old=q




pyplot.plot(distance_array,distance_store)
pyplot.show()