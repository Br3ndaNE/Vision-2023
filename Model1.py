import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import os
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Input
from keras.utils import img_to_array
from sklearn.model_selection import train_test_split

# Load the labels from the JSON file
with open('DatasetCarPlates/labels_resized.json', 'r') as f:
    data = json.load(f)

# Initialize dictionaries to hold images and labels
images = dict()
labels = dict()

# Loop to load and preprocess each image and its corresponding bounding box label
for i in range(433):
    car = f"Cars{i}"
    # Load images
    image_dir = "DatasetCarPlates/images/"
    image_path = os.path.join(image_dir, car + ".png") 
    images[car] = Image.open(image_path).convert('RGB')
    images[car] = images[car].resize((600, 400))  # Ensure all images have the same size
    images[car] = np.array(images[car])
    # Load bounding box
    xmin = data[car]["bndbox_resized"]["xmin"]
    xmax = data[car]["bndbox_resized"]["xmax"]
    ymin = data[car]["bndbox_resized"]["ymin"]
    ymax = data[car]["bndbox_resized"]["ymax"]

    labels[car] = [xmin, xmax, ymin, ymax]

# Convert the dictionaries to lists for easier processing
X = []
y = []

for car in images:
    X.append(images[car])
    y.append(labels[car])

# Convert lists to numpy arrays
X = np.array(X)
y = np.array(y)

print("Image data shape:", X.shape)
print("Label data shape:", y.shape)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Define the model
num_filters = 32
filter_size = (3, 3)
pool_size = (2, 2)

model = Sequential([
    Conv2D(num_filters, filter_size, activation='relu', input_shape=(400, 600, 3)),
    MaxPooling2D(pool_size),
    Conv2D(64, filter_size, activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, filter_size, activation='relu'),
    Flatten(),
    Dense(units=128, activation='relu'),
    Dense(units=4)  # Output layer for bounding box coordinates
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=1, validation_split=0.2)


predicted_bboxes = model.predict(X_test)

for pred, true in zip(predicted_bboxes, y_test):
    print(f'The true bbox of image  = {true} where as the predicted  = {pred}')



# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test loss: {loss}, Test accuracy: {accuracy}')
