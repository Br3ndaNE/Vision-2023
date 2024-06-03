from PIL import Image
import os

def resize_images(input_dir, output_dir, target_size):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through each image in the input directory
    for filename in os.listdir(input_dir):
        # Open the image
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path)
        
        # Resize the image to the target size
        img_resized = img.resize(target_size, Image.ANTIALIAS)
        
        # Save the resized image to the output directory
        output_path = os.path.join(output_dir, filename)
        img_resized.save(output_path)

# Example usage
input_directory = "DatasetNotScaled"
output_directory = "Dataset"
target_size = (1920, 1080)  # Specify the desired size here

resize_images(input_directory, output_directory, target_size)