import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread('image.jpg')
img=np.load("data.npy")
img=img.astype(np.uint8)

blur = cv2.bilateralFilter(img,9,75,75)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
