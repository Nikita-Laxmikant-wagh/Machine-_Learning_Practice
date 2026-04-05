import matplotlib.pyplot as plt

student_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi']
student_ages = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 40]

# Create a box plot
plt.boxplot(student_ages)

plt.xlabel('Students')
plt.ylabel('Ages')

# Add a title 
plt.title('Box Plot of Student Ages')

# Set x-ticks to show the label 'Ages' at position 1
plt.xticks([1], ['Ages'])
plt.show()
