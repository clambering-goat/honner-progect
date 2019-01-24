#import the necessary modules
#import the necessary modules
import freenect
import cv2
import numpy as np


#function to get depth image from kinect
def get_depth():
    array,_ = freenect.sync_get_depth()
    array = array.astype(np.uint8)

    return array



frame_array=[]
for q in range(50):

    #get a frame from depth sensor
    depth = get_depth()
    frame_array.append(depth)
    #display depth image





w, h = len(frame_array[q][0]), len(frame_array[q])

avarave_frame = np.zeros(shape=(h,w))

for q in range(50):
    for row in range(len(frame_array[q])-1):
        for cloum in range(len(frame_array[q][0])-4):
            avarave_frame[row][cloum]=avarave_frame[row][cloum]+frame_array[q][row][cloum]


for row in range(len(frame_array[q])-1):
    for cloum in range(len(frame_array[q][0])-4):
        avarave_frame[row][cloum]=avarave_frame[row][cloum]/50

print(type(avarave_frame))
while 1:
    array = avarave_frame.astype(np.uint8)
    cv2.imshow('Depth image',array)
    #in array each vaule is type <type 'numpy.uint8'>

    # quit program when 'esc' key is pressed
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
