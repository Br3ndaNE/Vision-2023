X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# # max base model
# num_filters = 32
# filter_size = (3, 3)
# pool_size = (2, 2)

# model = Sequential([
#     Conv2D(num_filters, filter_size, input_shape=(400, 600, 3)),
#     MaxPooling2D(pool_size),
#     Conv2D(64, filter_size, activation='relu'),  # Extra Convolutional Layer
#     MaxPooling2D((2, 2)),
#     Conv2D(128, filter_size, activation='relu'),  # Extra Convolutional Layer
#     Flatten(),
#     Dense(units=128, activation='relu'),
#     Dense(units=4)
# ])

# model.compile(optimizer='adam', metrics=['accuracy'])