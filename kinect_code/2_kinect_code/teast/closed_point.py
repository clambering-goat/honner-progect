import numpy as np

import os

list_of_vaule=[]

print("files found ")
for q in os.listdir("./"):

    if q[-4:len(q)]==".npy":
        print(q)
        d2d_to_1d=[]
        if q[0]=="d":
            image=np.load(q)
            count_x=1000
            count_y=1000
            vaule=1000

            for y in image:
                for x in y:
                    d2d_to_1d.append(x)
                    #print(x)
                    if vaule>x:# and x>10:
                        #print("new vaule given ",x)
                        vaule=x
                    if not x in list_of_vaule:
                        list_of_vaule.append(x)
            print(" ")
            print("for ",q)
            print("clesest point ",vaule)
            print("totol number of points ", len(d2d_to_1d))
            print("")


            list_of_vaule=sorted(list_of_vaule)
            groups=[]
            member_count=50
            avarge=0
            for vaule_found in list_of_vaule:
                #print(vaule_found,d2d_to_1d.count(vaule_found)
                avarge=avarge+d2d_to_1d.count(vaule_found)
            print("pre devid avarge ",avarge)
            avarge=avarge/ 255
            for vaule_found in list_of_vaule:

                if d2d_to_1d.count(vaule_found)>avarge:
                    groups.append(vaule_found)

            print(" ")
            print("group with move than ",avarge ," members ")
            for q in groups:
                print(q)
            # print(type(image))
            # name=q[:-4]+"_image.png"
            # #image=(image,cv2.COLOR_GRAY2RGB)
            # print(type(image))
            # #image = image.astype(np.uint8)
            # cv2.imwrite(name,image)
