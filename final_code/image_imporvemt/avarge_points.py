

import numpy as np
import cv2
import os
from PIL import Image
from scipy import stats
main_list={}
print("files found ")
shearch_loaction="G:\python_data\scaning_a_failed_print/"

scan_range=3

loop_count=0
for q in os.listdir(shearch_loaction):

    if q[-4:len(q)]==".npy" and q[0]=="d":
        print(q)
        loop_count += 1
        file_loaction=shearch_loaction+q
        image=np.load(file_loaction)

        for y in range(len(image)-1):
            for x in range(len(image[0])-1):
                key=y,x

                if  not key in main_list.keys():
                    main_list[key]=[]

                main_list[key].append(image[y][x])

    if loop_count==scan_range:
        break

y_count=-1
list_of_vaules=[]
range_vaile=np.zeros((480,640,3),dtype=np.uint8)
for q in main_list:

    range_data=main_list[q]
    vaule_max=np.max(range_data)
    vaule_min=np.min(range_data)
    tt=int((vaule_max - vaule_min))
    # tt = stats.mode(range_data)
    # tt=tt[0]
    # tt=tt[0]
    #tt=range_data[0]
    if not tt in list_of_vaules:
        list_of_vaules.append(tt)

    range_vaile[q[0]][q[1]]=[tt,tt,tt]


img = Image.fromarray(range_vaile,"RGB")

img.show()
img.save("iamges.png")