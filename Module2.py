from skimage import data, filters, feature
from skimage.viewer import ImageViewer
import numpy as np
import scipy
import matplotlib.pyplot as plt

image0 = data.camera()

gaus_filter_image = filters.gaussian(image0, 0.8 )

farid_filter = filters.farid(image0)
scharr_filter = filters.scharr(image0)
roberts_filter = filters.roberts(image0)


mask1=[[-1/9,0,1/9],[-1/9,0,1/9],[-1/9,0,1/9]]
mask2=[[-1/9,-1/9,-1/9], [0,0,0], [1/9,1/9,1/9]]

mask3=[[-1/9,0,1/9],[-2/9,0,2/9],[-1/9,0,1/9]]  
mask4=[[-1/9,-2/9,-1/9], [0,0,0], [1/9,2/9,1/9]]

laplactionoperator=[[0,-1,0], [-1,4,-1], [0,-1,0]]
laplactionoperator2=[[-1,-1,-1], [-1,8,-1], [-1,-1,-1]]

newimage0=scipy.ndimage.convolve(gaus_filter_image, mask1)                             #Prewitt
newimage1=scipy.ndimage.convolve(gaus_filter_image, mask2)                             #Prewitt

newimage2=scipy.ndimage.convolve(gaus_filter_image, mask3)                             #The Sobel
newimage3=scipy.ndimage.convolve(gaus_filter_image, mask4)                             #The Sobel

newimage4=scipy.ndimage.convolve(gaus_filter_image, laplactionoperator)                #The Laplacian
newimage5=scipy.ndimage.convolve(gaus_filter_image, laplactionoperator2)               #The Laplacian

dogwater_ass1 = np.sqrt( np.square( newimage0 ) + np.square( newimage1 ) )             #Prewitt
dogwater_ass2 = np.sqrt( np.square( newimage2 ) + np.square( newimage3 ) )             #The Sobel
dogwater_ass3= np.sqrt( np.square( newimage4 ) + np.square( newimage5 ) )              #The Laplacian

dogwater_ass4 = feature.canny(gaus_filter_image)
dogwater_ass5 = feature.canny(gaus_filter_image, 3)

fig = plt.figure(figsize=(16, 9))

result1 = fig.add_subplot(3, 3, 1)
result1.title.set_text('Canny with sigma 1')
result1.axis("off")
plt.imshow(dogwater_ass4, cmap="gray")

result2 = fig.add_subplot(3, 3, 2)
result2.title.set_text('Gaussian filter')
result2.axis("off")
plt.imshow(gaus_filter_image,cmap="gray")

result3 = fig.add_subplot(3, 3, 3)
result3.title.set_text('Canny with sigma 3')
result3.axis("off")
plt.imshow(dogwater_ass5, cmap="gray")

result4 = fig.add_subplot(3, 3, 4)
result4.title.set_text('Prewitt edge detection')
result4.axis("off")
plt.imshow(dogwater_ass1 ,cmap="gray")

result5 = fig.add_subplot(3, 3, 5)
result5.title.set_text('The soble edge detection')
result5.axis("off")
plt.imshow(dogwater_ass2, cmap="gray")

result6 = fig.add_subplot(3, 3, 6)
result6.title.set_text('The Laplacian edge detection')
result6.axis("off")
plt.imshow(dogwater_ass3, cmap="gray")

result7 = fig.add_subplot(3, 3, 7)
result7.title.set_text('Farid edge detection')
result7.axis("off")
plt.imshow(farid_filter, cmap="gray")

result8 = fig.add_subplot(3, 3, 8)
result8.title.set_text('Roberts edge detection')
result8.axis("off")
plt.imshow(roberts_filter, cmap="gray")

result9 = fig.add_subplot(3, 3, 9)
result9.title.set_text('Scharr edge detection')
result9.axis("off")
plt.imshow(scharr_filter, cmap="gray")


plt.show()