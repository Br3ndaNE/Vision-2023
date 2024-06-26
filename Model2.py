import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import os
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from sklearn.model_selection import train_test_split


for o in range(4, 6):
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
        # images[car] = Image.open(image_path).convert('L')
        images[car] = images[car].resize((600, 400)) 
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

    # Split the data into training and testing sets and normalize data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    X_train_normalized = (X_train / 255.0) - 0.5
    X_test_normalized = (X_test / 255.0) - 0.5

    # Create model #Compile fit predict model
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(400, 600, 3)),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(4)  
    ])

    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
    model.fit(X_train_normalized , y_train, epochs=75, validation_split=0.2)
    predicted_bboxes = model.predict(X_test_normalized)

    average_iou_lst = []
    max_iou = 0

    # Calculates IoU
    for pred, true in zip(predicted_bboxes, y_test):
        xmin1 = true[0]
        xmax1 = true[1]
        ymin1 = true[2]
        ymax1 = true[3] 
        
        xmin2 = pred[0] 
        xmax2 = pred[1] 
        ymin2 = pred[2] 
        ymax2 = pred[3] 

        xmin_inter = max(xmin1, xmin2)
        xmax_inter = min(xmax1, xmax2)
        ymin_inter = max(ymin1, ymin2)
        ymax_inter = min(ymax1, ymax2)
        
        intersection_area = max(0, xmax_inter - xmin_inter + 1) * max(0, ymax_inter - ymin_inter + 1)
        
        bbox1_area = (xmax1 - xmin1 + 1) * (ymax1 - ymin1 + 1)
        bbox2_area = (xmax2 - xmin2 + 1) * (ymax2 - ymin2 + 1)
        
        union_area = bbox1_area + bbox2_area - intersection_area
        iou = intersection_area / union_area
        average_iou_lst.append(iou)

        if(iou > max_iou):
            max_iou = iou

    #Writes value to file in folder
    with open(f'Model2_RGB\Model2_Test{o}_RGB\!Values_IOU.txt', 'w') as f:
        f.write("Average IOU values:\n")
        f.write(str(average_iou_lst) + '\n')
        f.write("Average: " + str(sum(average_iou_lst) / len(average_iou_lst)) + " %\n")
        f.write("Max IOU:\n")
        f.write(str(max_iou) + " %\n")

    Counter = 0
    # Boundingbox loop
    for pred, true, image_array in zip(predicted_bboxes, y_test, X_test):
        predicted_image = Image.fromarray(image_array.astype('uint8'))
        fig, ax = plt.subplots()
        ax.imshow(predicted_image)

        # Define rectangle arguments
        xmin1 = true[0]
        xmax1 = true[1]
        ymin1 = true[2]
        ymax1 = true[3] 
        
        xmin2 = pred[0] 
        xmax2 = pred[1] 
        ymin2 = pred[2] 
        ymax2 = pred[3] 

        #Rectangle for label value
        rect_width_true = xmax1 - xmin1
        rect_height_true= ymax1 - ymin1
        rect_true = patches.Rectangle((xmin1, ymin1), rect_width_true, rect_height_true, linewidth=1, edgecolor='b', facecolor='none')
        
        #Rectangle for predicted value
        rect_width_predicted = xmax2 - xmin2
        rect_height_predicted = ymax2 - ymin2
        rect_predicted = patches.Rectangle((xmin2, ymin2), rect_width_predicted, rect_height_predicted, linewidth=1, edgecolor='r', facecolor='none')

        ax.add_patch(rect_predicted)
        ax.add_patch(rect_true)

        plt.savefig(f'Model2_RGB\Model2_Test{o}_RGB\Cars{Counter}.png')
        plt.close()
        Counter += 1
