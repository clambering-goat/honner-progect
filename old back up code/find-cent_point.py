


#the opbebes is about 15cm from center
import numpy as np
import cv2
import os

import matplotlib.pyplot as plt



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

error_to_accept=4

count=0

line_mark_Width=-1




print("cent withd sacn ")
start_v=[]
end_v=[]





list_x=[]
list_y=[]
for q in depth_data:
    count+=1
    list_x = []
    print(count)
    cent_vaule=q[center_h][center_w]
    print("cent vaule is ",cent_vaule)
    size=0

    n_v=1

    for w in range(200):
        if q[center_h][center_w+w*n_v] >cent_vaule+error_to_accept or q[center_h][center_w+w*n_v]<cent_vaule-error_to_accept:
            print("edge found ",center_h,center_w+w,"vaule ",q[center_h][center_w+w])
            size=w
            start_v.append(center_w+w)

            break
        list_x.append(q[center_h][center_w + w * n_v])

    for w in range(200):
        if q[center_h][center_w-w*n_v] >cent_vaule+error_to_accept or q[center_h][center_w-w*n_v]<cent_vaule-error_to_accept:
            print("edge found ",center_h,center_w-w,"vaule ",q[center_h][center_w-w])
            size = w+size
            end_v.append(center_w-w)
            break

        list_x.append(q[center_h][center_w + w * n_v])

    plt.plot(list_x, 'ro')

    plt.axis([0, 300, 0, 300])
    plt.show()

    print("size ",size)


print("")
print(" sacn hight","\n")


count=0
start_h=[]
end_h=[]


for q in depth_data:
    count+=1
    list_x = []
    print(count)
    cent_vaule=q[center_h][center_w]

    for w in range(200):
        list_x.append(q[center_h][center_w + w * n_v])
        if q[center_h+w][center_w] >cent_vaule+3 or q[center_h+w][center_w]<cent_vaule-3:
            print("edge found ",center_h+w,center_w,"vaule ",q[center_h+w][center_w])
            size=w
            start_h.append(center_h+w)

            break


    for w in range(200):
        list_x.append(q[center_h][center_w + w * n_v])
        if q[center_h-w][center_w] >cent_vaule+3 or q[center_h-w][center_w]<cent_vaule-3:
            print("edge found ",center_h-w,center_w,"vaule ",q[center_h-w][center_w])
            size = w + size
            end_h.append(center_h-w)

            break


    plt.plot(list_x, 'ro')

    plt.axis([0, 300, 0, 300])
    plt.show()


q=-1
for images in depth_data:
    q=q+1
    cv2.line(images,(start_v[q],240),(end_v[q],240),(125,0,125),5)
    cv2.line(images, (240, start_h[q]), (240, end_h[q]), (125, 0, 125), 5)





def big_swap(v1,v2):
    if v2 < v1:
        temp=v1
        v1=v2
        v2=temp
    return(v1,v2)

image_1,image_2=depth_data
box_1=(start_v[0],end_v[0],start_h[0],end_h[0])
box_2=(start_v[1],end_v[1],start_h[1],end_h[1])









v1,v2=big_swap(box_1[0],box_1[1])
v3,v4=big_swap(box_1[2],box_1[3])


count=0
avarge_1=0


for y_scan in range(v3,v4):
    for x_scan in range(v1,v2):
        count=count+1

        avarge_1=image_1[y_scan][x_scan]+avarge_1


avarge_1=avarge_1/count

print("arage point for image 1 ",avarge_1)





v1,v2=big_swap(box_2[0],box_2[1])
v3,v4=big_swap(box_2[2],box_2[3])


count=0
avarge_2=0


for y_scan in range(v3,v4):
    for x_scan in range(v1,v2):
        count=count+1

        avarge_2=image_1[y_scan][x_scan]+avarge_2


avarge_2=avarge_2/count

print("arage point for image 2 ",avarge_2)











''' 
for q in depth_data:
    cv2.imshow('image',q)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("size ",size)
'''






print("done ")
