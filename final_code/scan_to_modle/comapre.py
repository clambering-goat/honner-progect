import rotated_object






files="./point_cloud.xyz"
file_in=open(files,"r")

fiel_in_data=file_in.readlines()
file_in.close()

#need roastend -90 to be sacn and kinect sacn

axies="x"
name = files[0:-4]+axies+"rotaion.xyz"
file_out=open(name,"w")


point_count_rotaion=rotated_object.roatation(-90,axies,fiel_in_data,file_out)







print("hi ")