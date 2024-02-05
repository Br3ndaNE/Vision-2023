import skimage
# from skimage.viewer import ImageViewer
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

image = io.imread("2023\images\phote1.jpg")

hsv_image = skimage.color.rgb2hsv(image)
histogram_array_filtered = []
histogram_array_filtered_not = []

for colors in hsv_image:
    for color in colors:
        hue = color[0] * 360
        histogram_array_filtered_not.append(hue)


for colors in hsv_image:
    for color in colors:
        hue = color[0] * 360
        if 250 < hue or hue < 170:
            color[1] = 0
        else:
            histogram_array_filtered.append(color[0] * 360)


rgb_image = skimage.color.hsv2rgb(hsv_image)

fig = plt.figure(figsize=(10, 7))

fig.add_subplot(2, 2, 1)
plt.imshow(image)

fig.add_subplot(2, 2, 2)
plt.hist(histogram_array_filtered_not, bins=360, range=(0,360))

fig.add_subplot(2, 2, 3)
plt.imshow(rgb_image)

fig.add_subplot(2, 2, 4)
plt.hist(histogram_array_filtered, bins=360, range=(0,360))
plt.show()
