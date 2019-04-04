

import numpy as np
import cv2
import os

floder_name=input("floder look in ")
#floder_name="temp"
dir_to_look="G:/python_data/"+floder_name+"/"

def scan():
    list_scan=[]
    for q in os.listdir(dir_to_look):
        if q[-4:len(q)] == ".npy" and q[0]=="d":
            list_scan.append(q)

    return (list_scan)


hightest_number=0
second_higherst=0
while True:


    data=scan()

    for q in data:
        vaule=q.split("_")
        number=vaule[-1]
        number=number[0:-4]
        number =int(number)
        if number>hightest_number:
            hightest_number=number

        if number>second_higherst and number !=hightest_number:
            second_higherst=number



    if second_higherst!=0:
        file_pre=data[0]
        file_pre=file_pre
        pre=""
        for q in file_pre:
            pre=pre+q

        pre=pre.split("_")
        #pre=pre[0]
        pre_2=""
        for q in pre[0:-1]:
            pre_2=pre_2+q+"_"

        image=np.load(dir_to_look+pre_2+str(second_higherst)+".npy")

        image = image.astype(np.uint8)
        cv2.imshow("frame",image)
        cv2.waitKey(5)

#depth_carmea('192.168.1.212', 36408)_101.npy