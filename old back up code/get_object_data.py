


#the object edge  is about 15cm from center
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

line_mark_Width=-1




print("cent withd sacn ")
start=0
end=0

start_2=0
end_2=0

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
            start=center_w+w
            break


    for w in range(200):
        if q[center_h][center_w-w] >cent_vaule+error_to_accept or q[center_h][center_w-w]<cent_vaule-error_to_accept:
            print("edge found ",center_h,center_w-w,"vaule ",q[center_h][center_w-w])
            size = w+size
            end=center_w-w
            break


    #uncomment to see vertial lines
    #cv2.line(q,(start,240),(end,240),(125,0,125),5)
    cv2.imshow('image',q)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("size ",size)
print(" sacn hight","\n")


count=0

start_2=0
end_2=0

for q in depth_data:
    count+=1

    print(count)
    cent_vaule=q[center_h][center_w]
    print("cent vaule is ",cent_vaule)
    for w in range(200):
        if q[center_h+w][center_w] >cent_vaule+3 or q[center_h+w][center_w]<cent_vaule-3:
            print("edge found ",center_h+w,center_w,"vaule ",q[center_h+w][center_w])
            size=w
            start_2=center_h+w
            break


    for w in range(200):
        if q[center_h-w][center_w] >cent_vaule+3 or q[center_h-w][center_w]<cent_vaule-3:
            print("edge found ",center_h-w,center_w,"vaule ",q[center_h-w][center_w])
            size = w + size
            end_2=center_h-w
            break




    cv2.line(q,(240,start_2),(240,end_2),(125,0,125),5)
    cv2.imshow('image',q)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("size ",size)







print("done ")
