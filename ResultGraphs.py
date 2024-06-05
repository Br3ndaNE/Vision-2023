import matplotlib.pyplot as plt


values = [0.29241707587747534, 0.36224228039899514, 0.2073620015190266, 0.2773226619308108, 0.27946043545206256] #model 1 RGB


# Calculate the average of the values
average_value = sum(values) / len(values)

# Create x-axis values
x_values = list(range(1, len(values) + 1))

# Plot the line graph
plt.plot(x_values, values, marker='o')

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