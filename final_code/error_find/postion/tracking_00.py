

import numpy as np
import cv2

data_input=np.load("data_2.npy")
given_center_point=335, 269


#max_vaule=948
#min_vaule=748

z_offster_from_cal_file=31.58





given_z_dixstance= 817

start_pixsel_y_offste=z_offster_from_cal_file/(1.64*(given_z_dixstance/1000))


start_0_0_point=int(given_center_point[0]),int(given_center_point[1]+start_pixsel_y_offste)



print("starting at points ", start_0_0_point)



def get_y_center_pount(z_distance):

    new_pixesl_offset=z_offster_from_cal_file/(1.64*(z_distance/1000))
    new_pixesl_offset=int(new_pixesl_offset)
    return new_pixesl_offset




mins=get_y_center_pount(708)
maxs=get_y_center_pount(998)

print("mins max",mins,maxs)

data_input=data_input.astype(np.uint8)



start_line=given_center_point[0],given_center_point[1]+mins
end_line=given_center_point[0],given_center_point[1]+maxs





data_input = cv2.cvtColor(data_input,cv2.COLOR_GRAY2RGB)
cv2.line(data_input,start_line,end_line,(255,0,0),2)

cv2.imshow("frame",data_input)

cv2.waitKey(0)

cv2.destroyAllWindows()


