import numpy as np
import matplotlib.pyplot as plt

from skimage.filters import gaussian
from skimage.segmentation import active_contour
from skimage import io

#img = data.astronaut()
#img = rgb2gray(img)

#image_name="depth_carmea('192.168.1.106', 60892)_24809_image.png"
image_name="depth1_image.png"
img = io.imread(image_name)

y_max=len(img)
x_max=len(img[0])

s = np.linspace(0, 2*np.pi, 400)


x = x_max/2 + 100*np.cos(s)
y = y_max/2 + 100*np.sin(s)


init = np.array([x, y]).T

snake = active_contour(gaussian(img, 3),
                       init, alpha=0.04, beta=20, gamma=0.001)

fig, ax = plt.subplots(figsize=(7, 7))
ax.imshow(img, cmap=plt.cm.gray)
ax.plot(init[:, 0], init[:, 1], '--r', lw=3)
ax.plot(snake[:, 0], snake[:, 1], '-b', lw=3)
ax.set_xticks([]), ax.set_yticks([])
ax.axis([0, img.shape[1], img.shape[0], 0])
plt.show()

