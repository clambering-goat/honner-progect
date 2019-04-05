import numpy as np
import os








# dir_to_look="C:/Users/back up/Documents/GitHub/honner-progect/point _colder for digrasms/numpy_data/"
#
# dir_to_save="C:/Users/back up/Documents/GitHub/honner-progect/point _colder for digrasms/xyz_data/"

dir_to_look="D:/scan_notes/ver_shift/startit_oin/"
dir_to_save="D:/scan_notes/ver_shift/startit_oin/"
for files in os.listdir(dir_to_look):
    if files[-4:len(files)]==".npy" and files[0]=="d":
        data=np.load(dir_to_look+files)

        file_name=files[0:-4]
        file_name=dir_to_save+file_name+".xyz"

        file = open(file_name, "w")
        print(file_name)
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

        print("done file ",files)
