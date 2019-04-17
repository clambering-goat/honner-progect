import g_code_to_point_cloud
import point_could_to_x_min_max


import os


teast_mode=True

#step 1 -file_seletion


if teast_mode==False:
    while 1:
        user_input=input("please enter the  dir of the data")
        if os.path.isdir(user_input)==True:
            break
        else:
            print("invaild dir ")
else:
    user_input="./"


list_of_files=[]
for files in os.listdir(user_input):
    if files[-6:len(files)] == ".gcode":

        list_of_files.append(files)


file_to_open=""

if len(list_of_files)==0:
    print("no files found ")
    exit()

elif len(list_of_files) ==1:
    file_to_open=list_of_files[0]



elif len(list_of_files)>1:
    print("files found :")
    count=0
    for q in list_of_files:
        count+=1
        print(count,q)

    while 1:
        user_input=input("please enter the  number of the file you want to open")


        try:
            user_input=int(user_input)
            list_of_files[user_input]
            file_selected= user_input - 1
            file_to_open = list_of_files[file_selected]
            break

        except:
            print("invaild input ")

# print("start g code to point cloude convert on: ",file_to_open)
# step_1=g_code_to_point_cloud.g_code_to_point_cloud(file_to_open)
# file_name_of_point_could=step_1.get_file_name()
# print("point could make and saved to file ",file_name_of_point_could)


file_name_of_point_could="point_cloud_of_changin_in_depth_teast.xyz"
print("finding max and min x points ")
step_2=point_could_to_x_min_max.get_x_min_to_x_max(file_name_of_point_could)
max_min_x=step_2.get_file_name()
print("max and min x point found saved to file ",max_min_x)
