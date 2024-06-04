import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import os
# Path to the directory containing the images
number = 0
for i in range(50):
    car = f"Cars{i}"
    image_dir = "DatasetCarPlates/images/"
    image_path = os.path.join(image_dir, car + ".png")  # Replace "example.jpg" with your image file name

    # Load JSON data
    with open('DatasetCarPlates/labels_resized.json', 'r') as f:
        data = json.load(f)

    # Load the image
    image = Image.open(image_path)

    # Create figure and axis
    fig, ax = plt.subplots()

    # Display the image
    ax.imshow(image)

    # Loop through each car in the JSON data

    xmin = data[car]["bndbox_resized"]["xmin"]
    xmax = data[car]["bndbox_resized"]["xmax"]
    ymin = data[car]["bndbox_resized"]["ymin"]
    ymax = data[car]["bndbox_resized"]["ymax"]

    # Calculate rectangle width and height
    rect_width = xmax - xmin
    rect_height = ymax - ymin

    # Create a rectangle patch
    rect = patches.Rectangle((xmin, ymin), rect_width, rect_height, linewidth=1, edgecolor='r', facecolor='none')

    # Add the rectangle patch to the axis
    ax.add_patch(rect)

    # Show the plot
    plt.show()
