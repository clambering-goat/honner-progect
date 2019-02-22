# examples/Python/Tutorial/Basic/pointcloud.py

import numpy as np
from open3d  import *
import os


list_of_point_cloud_found=[]
for files in os.listdir():

    if files[-4:len(files)]==".xyz":
        list_of_point_cloud_found.append(files)

print("list_of_point_cloud_found")
count=0
for point_cloud_found in list_of_point_cloud_found:
    count=count+1
    print(count," ",point_cloud_found)



if len(list_of_point_cloud_found)>1:
    choise=input("pick one using numbers ")
    choise=int(choise)
    choise=choise-1

elif len(list_of_point_cloud_found)<1:
    print(" no data found closing ")
    exit()
else:
    choise=0


file_to_load=list_of_point_cloud_found[choise]
try:
    pcd = read_point_cloud(file_to_load)
    print(pcd)
    print(np.asarray(pcd.points))
    draw_geometries([pcd])
except:
    print("error in block 1")
