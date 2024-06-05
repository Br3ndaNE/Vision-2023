import matplotlib.pyplot as plt


model1_RGB_values = [0.29241707587747534, 0.36224228039899514, 0.2073620015190266, 0.2773226619308108, 0.27946043545206256] #model 1 RGB
model1_Greyscale_values = [0.3227117077577404, 0.282611827373081, 0.30147471693019134, 0.312549068818445, 0.3009616529654942] #model 1 RGB
model2_RGB_values = [0.2713153557094071, 0.29315073730550517, 0.3591017085437702,  0.266927130595351, 0.32667393169242304] #model 1 RGB
model2_Greyscale_values = [0.34382378332751895, 0.31661627520811025, 0.23534355227786727, 0.36455666138115206, 0.3373841502163967]

# Calculate the average of the values
average_value = sum(model2_RGB_values) / len(model2_RGB_values)

# Create x-axis values
x_values = list(range(1, len(model2_RGB_values) + 1))

# Plot the line graph
plt.plot(x_values, model2_RGB_values, marker='o')

# Add a horizontal line for the average value
plt.axhline(y=average_value, color='r', linestyle='--', label='Average of the average IoU values')

# Add a title and labels
plt.title('')
plt.xlabel('Iterations')
plt.ylabel('Average IoU')

# Set the x-axis ticks to show steps from 1 to 5
plt.xticks(x_values)

# Show the legend
plt.legend()

# Show the plot
plt.show()