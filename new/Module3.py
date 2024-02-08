import numpy as np
import matplotlib.pyplot as plt
from skimage import data, transform, io

def show_images(image_before, image_after, title_before='Before', title_after='After'):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.imshow(image_before, cmap='gray')
    ax1.set_title(title_before)
    ax1.axis('off')
    ax2.imshow(image_after, cmap='gray')
    ax2.set_title(title_after)
    ax2.axis('off')
    plt.show()

# Load example image
image = io.imread("new\images\monkey.jpg")

angle = 30
rotation_matrix = transform.AffineTransform(rotation=np.deg2rad(angle))
image_rotated = transform.warp(image, rotation_matrix)
show_images(image, image_rotated, title_before='Original', title_after=f'Rotated by {angle} degrees')

translation = (20, -10)
translation_matrix = transform.AffineTransform(translation=translation)
image_translated = transform.warp(image, translation_matrix)
show_images(image, image_translated, title_before='Original', title_after=f'Translated by {translation}')

scale = (0.5, 1.5)
stretch_matrix = transform.AffineTransform(scale=scale)
image_stretched = transform.warp(image, stretch_matrix)
show_images(image, image_stretched, title_before='Original', title_after=f'Stretched by {scale}')

