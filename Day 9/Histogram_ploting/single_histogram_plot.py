import matplotlib.pyplot as plt
import numpy as np

marks = [10, 15, 20, 25, 28, 30, 35,39, 40, 43, 47, 50, 55]

# Create a histogram
# bins=15 means we want to divide the data into 15 equal intervals
plt.hist(marks, bins=15, edgecolor='black', color='skyblue')

# Add labels to the axes
plt.xlabel('Marks')
plt.ylabel('Frequency')

# Add a title and legend
plt.title('Distribution of Student Marks')
plt.legend(['Marks'])
plt.show()