import matplotlib.pyplot as plt

students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
scores = [85, 90, 78, 92, 88]

# Define explode values to highlight specific slices
explode_values = [0.1, 0, 0.4, 0, 0]

# Create a pie chart with custom styling
plt.pie(scores, labels=students, autopct='%1.1f%%', startangle=140,
        
          wedgeprops={           # Custom styling for the pie slices
              "edgecolor": 'black',
            "linewidth": 1,
            "linestyle": '--'
          } 
            , explode=explode_values    # Highlight specific slices with explode values
          )

# Add a title and ensure the pie chart is circular
plt.title('Student Scores Distribution')
plt.axis('equal')  
plt.show()
