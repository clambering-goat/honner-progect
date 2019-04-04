
import cv2
import numpy as np
import os

#tracker = cv2.TrackerCSRT_create()
#tracker = cv2.TrackerMIL_create()
tracker = cv2.TrackerTLD_create()

frame_list=[]

home="D:/scan_notes/vido/"
for q in os.listdir(home):
    data=np.load(home+q)
    data = data.astype(np.uint8)
    frame_list.append(data)

bbox = cv2.selectROI(frame_list[0], False)
ok = tracker.init(frame_list[0], bbox)
for frame in frame_list:

    # Initialize tracker with first frame and bounding box

    frame = cv2.GaussianBlur(frame, (5, 5), 0)
    ok, bbox = tracker.update(frame)

    p1 = (int(bbox[0]), int(bbox[1]))
    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
    cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
    cv2.imshow("Tracking", frame)
    cv2.waitKey(500)