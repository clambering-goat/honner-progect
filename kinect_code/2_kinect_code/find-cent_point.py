


#the opbebes is about 15cm from center
import numpy as np
import cv2
import os



image_data=[]
depth_data=[]
print("files found ")
for q in os.listdir("./"):

    if q[-4:len(q)]==".npy":
        data=np.load(q)
        print(q)
        if q[0]=="c":
            image_data.append(data)
        if q[0]=="d":
            depth_data.append(data)




d_hight,d_width=len(depth_data[0]),len(depth_data[0][0])

c_hight,c_width=len(image_data[0]),len(image_data[0][0])


center_h,center_w=240,320

'''

count=0
for q in depth_data:
    count+=1
    print(count)
    for w in range(20):
        print(q[center_h][center_w+w])

    for w in range(20):
        print(q[center_h][center_w-w])
'''

error_to_accept=10

count=0

line_mark_Width=500




print("cent withd sacn ")
for q in depth_data:
    count+=1
    print(count)
    cent_vaule=q[center_h][center_w]
    print("cent vaule is ",cent_vaule)
    size=0
    for w in range(200):
        if q[center_h][center_w+w] >cent_vaule+error_to_accept or q[center_h][center_w+w]<cent_vaule-error_to_accept:
            print("edge found ",center_h,center_w+w,"vaule ",q[center_h][center_w+w])
            size=w
            break


    for w in range(200):
        if q[center_h][center_w-w] >cent_vaule+error_to_accept or q[center_h][center_w-w]<cent_vaule-error_to_accept:
            print("edge found ",center_h,center_w-w,"vaule ",q[center_h][center_w-w])
            size = w+size
            break


    print("size ",size)
print(" sacn hight","\n")


count=0

line_mark_Width=600

for q in depth_data:
    count+=1
    print(count)
    cent_vaule=q[center_h][center_w]
    print("cent vaule is ",cent_vaule)
    for w in range(200):
        if q[center_h+w][center_w] >cent_vaule+3 or q[center_h+w][center_w]<cent_vaule-3:
            print("edge found ",center_h+w,center_w,"vaule ",q[center_h+w][center_w])
            size=w
            break


    for w in range(200):
        if q[center_h-w][center_w] >cent_vaule+3 or q[center_h-w][center_w]<cent_vaule-3:
            print("edge found ",center_h-w,center_w,"vaule ",q[center_h-w][center_w])
            size = w + size
            break
    print("size ",size)



print("done ")
