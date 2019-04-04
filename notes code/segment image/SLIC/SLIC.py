import numpy as np
import matplotlib.pyplot as plt

from skimage.filters import gaussian
from skimage.segmentation import slic
import skimage.color as color
from skimage import io
from skimage import data
import numpy as np



import matplotlib.pyplot as plt

image_name="depth1_image.png"
img = io.imread(image_name)

image_slic = slic(img,n_segments=1000)
def image_show(image, nrows=1, ncols=1, cmap='gray'):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, 14))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    return fig, ax

image_show(color.label2rgb(image_slic, img, kind='avg'));

plt.show()