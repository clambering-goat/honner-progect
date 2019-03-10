
import numpy as np
import os



dir_to_look="G:/python_data/base_line/"

arrays=[]
count_frames=0


tt=True

for files in os.listdir(dir_to_look):
    if files[-4:len(files)]==".npy" and files[0]=="d":

        data=np.load(dir_to_look+files)

        arrays.append(data)


aravarge_array=[]

for array_count in range(len(data)-1):
    for array_count2 in range(len(data)-1):
        if array_count==array_count2:
            pass
            #break
        match = 0
        count = 0

        array_1=arrays[array_count]
        array_2 = arrays[array_count2]

        for y in range(len(array_1)-1):
            for x in range(len(array_1[0])-1):
                if array_1[y][x]==array_2[y][x]:
                    match+=1

                count+=1
        aravarge=match/(count)
        print("arage",aravarge)
        aravarge_array.append(aravarge)

totoa=0
for q in aravarge_array:
    totoa+=q



totoa=totoa/len(aravarge_array)
print("avarge", totoa)

