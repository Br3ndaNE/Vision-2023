from skimage import data, filters, color
from skimage.viewer import ImageViewer
import numpy as np
import scipy
from scipy import ndimage
import matplotlib.pyplot as plt

image = data.camera()

filter = filters.gaussian(image, 0.8 )

mask1=[[-1/9,0,1/9],[-1/9,0,1/9],[-1/9,0,1/9]]
mask2=[[-1/9,-1/9,-1/9], [0,0,0], [1/9,1/9,1/9]]

newimage0=scipy.ndimage.convolve(filter, mask1)
newimage1=scipy.ndimage.convolve(filter, mask2)

dogwater_ass = np.sqrt( np.square( newimage0 ) + np.square( newimage1 ) )

fig = plt.figure(figsize=(16, 9))

fig.add_subplot(1, 4, 1)
plt.imshow(filter)

fig.add_subplot(1, 4, 2)
plt.imshow(newimage0)

fig.add_subplot(1, 4, 3)
plt.imshow(newimage1)

fig.add_subplot(1, 4, 4)
plt.imshow(dogwater_ass)

plt.show()