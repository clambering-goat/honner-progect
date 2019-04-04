import cv2
import math


image_name="depth1_image.png"
image_data=cv2.imread(image_name)



depth_mid=[]
for y in image_data:
    for x in y :
        depth_mid.append(x[0])


for i in range(len(depth_mid)-1):
    into_garma=depth_mid[i]
    vaule=math.gamma(into_garma)

    lb=vaule & 0xff

    if(vaule==0):
        depth_mid[3 * i + 0] = 255;
        depth_mid[3 * i + 1] = 255 - lb;
        depth_mid[3 * i + 2] = 255 - lb;
        #break;

    elif(vaule==1):

        depth_mid[3 * i + 0] = 255;
        depth_mid[3 * i + 1] = lb;
        depth_mid[3 * i + 2] = 0;
        #break;

    elif(vaule==2):

        depth_mid[3 * i + 0] = 255 - lb;
        depth_mid[3 * i + 1] = 255;
        depth_mid[3 * i + 2] = 0;
        #break;

    elif(vaule==3):

        depth_mid[3 * i + 0] = 0;
        depth_mid[3 * i + 1] = 255;
        depth_mid[3 * i + 2] = lb;
        #break;

    elif(vaule==4):

        depth_mid[3 * i + 0] = 0;
        depth_mid[3 * i + 1] = 255 - lb;
        depth_mid[3 * i + 2] = 255;
        #break;

    elif(vaule==5):

        depth_mid[3 * i + 0] = 0;
        depth_mid[3 * i + 1] = 0;
        depth_mid[3 * i + 2] = 255 - lb;
        #break;

    else:
        depth_mid[3 * i + 0] = 0;
        depth_mid[3 * i + 1] = 0;
        depth_mid[3 * i + 2] = 0;
        #break;



output=[]
y_count=-1
for y in image_data:
    x_count=-1
    y_count+=1
    output.append([])
    for x in y :
        x_count+=1
        output[y][x]=depth_mid[y*len(image_name[0]+x)]


cv2.imshow("frame",output)