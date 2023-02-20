from skimage import data, filters, color
from skimage.viewer import ImageViewer
import numpy as np
import scipy
from scipy import ndimage

image = data.camera()
viewer = ImageViewer(image)
viewer.show()

filter = filters.gaussian(image, 0.1)

mask1=[[-1/9,0,1/9],[-1/9,0,1/9],[-1/9,0,1/9]]
mask2=[[-1/9,-1/9,-1/9], [0,0,0], [1/9,1/9,1/9]]

newimage0=scipy.ndimage.convolve(filter, mask1)
newimage1=scipy.ndimage.convolve(filter, mask2)

dogwater_ass = np.sqrt(np.square(newimage0) + np.square(newimage1))

viewer = ImageViewer(dogwater_ass)
viewer.show()