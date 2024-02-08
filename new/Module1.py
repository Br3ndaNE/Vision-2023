import matplotlib.pyplot as plt
# from skimage import data
from skimage import io
from skimage.color import rgb2hsv
from skimage.color import hsv2rgb

rgbImage = io.imread("2023\images\monkey.jpg")
hsvImage = rgb2hsv(rgbImage)

for firstloop in hsvImage:
    for secondloop in firstloop:
        hueValue = (secondloop[0] * 360)
        # print(hueValue)
        if not((hueValue > 50) and (hueValue <  80)):
            secondloop[1] = 0

newRgbImage = hsv2rgb(hsvImage)
        


plt.imshow(newRgbImage)
plt.show()

