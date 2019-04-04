
import numpy as np
import os



dir_to_look="G:/python_data/base_line/"

avrage_frame=np.zeros((480,640))

count_frames=0
for files in os.listdir(dir_to_look):
    if files[-4:len(files)]==".npy" and files[0]=="d":
        data=np.load(dir_to_look+files)
        count_frames+=1
        avrage_frame=np.add(avrage_frame,data)



avrage_frame=np.true_divide(avrage_frame,count_frames)
np.save("avarge_frames",avrage_frame)





