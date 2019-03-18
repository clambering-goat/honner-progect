import cv2
import numpy as np

if __name__ == '__main__':
    # Read image
    im = cv2.imread("image.jpg")

    # Select ROI
    r = cv2.selectROI(im)

    # Crop image
    imCrop = im[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
    v_x1=int(r[1])
    v_x2=int(r[1] + r[3])
    v_y1=int(r[0])
    v_y2=int(r[0] + r[2])
    print("zone select ",v_x1,v_x2,v_y1,v_y2)
    # Display cropped image
    cv2.imshow("Image", imCrop)
    cv2.waitKey(0)