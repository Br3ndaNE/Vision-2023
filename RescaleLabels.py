import json

with open('DatasetCarPlates/labels.json', 'r') as f:
    data = json.load(f)

for car_id, car_data in data.items():
    raw_width = int(car_data["size"]["width"])
    raw_height = int(car_data["size"]["height"])
    factor_x = 600 / raw_width
    factor_y = 400 / raw_height

    raw_bndbox = car_data["bndbox"]
    raw_xmin = int(raw_bndbox["xmin"])
    raw_xmax = int(raw_bndbox["xmax"])
    raw_ymin = int(raw_bndbox["ymin"])
    raw_ymax = int(raw_bndbox["ymax"])

    resized_xmin = raw_xmin * factor_x
    resized_xmax = raw_xmax * factor_x
    resized_ymin = raw_ymin * factor_y
    resized_ymax = raw_ymax * factor_y

    car_data["bndbox_resized"] = {
        "xmin": resized_xmin,
        "xmax": resized_xmax,
        "ymin": resized_ymin,
        "ymax": resized_ymax
    }

# Writing the modified data back to the JSON file
with open('DatasetCarPlates/labels_resized.json', 'w') as f:
    json.dump(data, f, indent=4)


from PIL import Image
import os

# Path to the directory containing the images
image_dir = "DatasetCarPlates/images/"

# New dimensions
new_width = 600
new_height = 400

# Loop through all images in the directory
for filename in os.listdir(image_dir):
    # Check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Open the image
        image_path = os.path.join(image_dir, filename)
        image = Image.open(image_path)
        
        # Resize the image
        resized_image = image.resize((new_width, new_height))
        
        # Save the resized image, overwriting the original
        resized_image.save(image_path)

print("All images resized to", new_width, "x", new_height)