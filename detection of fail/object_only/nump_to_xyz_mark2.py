import numpy as np
import os








dir_to_look="G:/python_data/base_line/"
count_frames=0


for files in os.listdir(dir_to_look):
    if files[-4:len(files)]==".npy" and files[0]=="d":
        data=np.load(dir_to_look+files)
        count_frames+=1

        file = open("./xyz_data/kinect_point_cloud_"+str(count_frames)+".xyz", "w")

        x_p=-1
        y_p=-1
        for y in data:
            y_p+=1
            x_p=-1
            for z_data in y:
                x_p+=1
                transpotion=z_data
                data=str(x_p)+" "+str(y_p)+" "+str(transpotion)+" \n"
                file.write(data)
        file.close()
