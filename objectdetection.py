import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

# # Generate dummy data
# def generate_dummy_data(num_samples, img_size):
#     X = np.random.rand(num_samples, img_size, img_size, 3)
#     y = np.random.rand(num_samples, 4)  # [x_min, y_min, x_max, y_max]
#     return X, y

# # Define image size and number of samples
# img_size = 64
# num_samples = 1000

# # Generate data
# X, y = generate_dummy_data(num_samples, img_size)

# # Split data into training and testing sets
# split = int(0.8 * num_samples)
# X_train, X_test = X[:split], X[split:]
# y_train, y_test = y[:split], y[split:]

# # Build the model
# model = Sequential([
#     Conv2D(32, (3, 3), activation='relu', input_shape=(img_size, img_size, 3)),
#     MaxPooling2D((2, 2)),
#     Conv2D(64, (3, 3), activation='relu'),
#     MaxPooling2D((2, 2)),
#     Conv2D(128, (3, 3), activation='relu'),
#     MaxPooling2D((2, 2)),
#     Flatten(),
#     Dense(128, activation='relu'),
#     Dense(4)  # Output layer for bounding box coordinates
# ])

# # Compile the model
# model.compile(optimizer=Adam(), loss='mean_squared_error')

# # Train the model
# model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# # Evaluate the model
# loss = model.evaluate(X_test, y_test)
# print(f'Test loss: {loss}')

# # Predict bounding boxes on new images
# predictions = model.predict(X_test)

# # Plot a few test images with predicted bounding boxes
# def plot_image_with_bbox(image, bbox):
#     plt.imshow(image)
#     x_min, y_min, x_max, y_max = bbox
#     plt.gca().add_patch(plt.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min, 
#                                       edgecolor='red', facecolor='none', linewidth=2))
#     plt.show()

# # Plot first 5 test images with predicted bounding boxes
# for i in range(5):
#     plot_image_with_bbox(X_test[i], predictions[i])
