import cv2
import numpy as np

ix,iy = -1,-1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
        ix,iy = x,y

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)


for q in range(100):
    img[250][q]=(255,255,255)
img2=img.copy(img.all())
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        print (ix,iy)
cv2.destroyAllWindows()
while 1:
    cv2.imshow('image', img2)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()

def sacn():
    for l1 in img:
        for l2 in l1:
            for q in l2:
                if q!=0:
                    print("img is conatat")
                    return()

def sscn2():
    for l1 in img2:
        for l2 in l1:
            for q in l2:
                if q!=0:
                    print("img2 contnaeed ")
                    return()

sacn()
sscn2()