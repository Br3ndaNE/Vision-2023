from skimage import data,io
from matplotlib import pyplot as plt

image = data.camera()
io.imshow(image)
plt.show()