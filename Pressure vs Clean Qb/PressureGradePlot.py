import csv
import pandas as pd
import matplotlib.pyplot as plt

# Import Pressure CSV file
pressure_data = "passing_pressure.csv"

# Open CSV file and read data
with open(pressure_data, 'r', newline='') as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip the header row
    data = []

    # Loop through data
    for row in reader:
        name = row[0]
        pressure_grade = row[5]
        clean_grade = row[6]
        num_dropbacks = int(row[7])
        
        # Add validation to check for non-empty strings before converting to float
        if pressure_grade and clean_grade and num_dropbacks >= 5:
            pressure_grade = float(pressure_grade)
            clean_grade = float(clean_grade)
            data.append([name, pressure_grade, clean_grade, num_dropbacks])

# Creating The Plot

# Set x and y to empty lists
name = []
x = []
y = []

# Loop through new data and set to X and Y
for qb_grade in data:
    name.append(qb_grade[0])  # Use qb_grade[0] for player name
    x.append(qb_grade[2])     # Use qb_grade[2] for clean_grade
    y.append(qb_grade[1])     # Use qb_grade[1] for pressure_grade

# Put x, y into dictionary
xy = pd.DataFrame({'name': name, 'x': x, 'y': y})

# Define the plot
fig, ax = plt.subplots()

ax.scatter(xy['x'], xy['y'], s=20, c='red')

# Move left y-axis and bottom x-axis to center, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Set x and y axis limits
plt.xlim((20, 100))
plt.ylim((20, 100))

# Add labels for axes
plt.xlabel('Clean PFF Grade', size=6, color = 'Green')
plt.ylabel('Under Pressure PFF Grade', size=6, color = 'Red')

# Annotate with QB name and year
for i in xy.index:
    plt.annotate(f"{xy['name'][i]}", (xy['x'][i] + .35, xy['y'][i] + .5), fontsize=4)

plt.annotate('Great Clean and Pressured', (90,90), fontsize=7, color = 'green')
plt.annotate('Great Pressured but not Clean?', (20,90), fontsize=7, color = 'purple')
plt.annotate('Poor Clean and Pressured', (20,25), fontsize=7, color = 'red')
plt.annotate('Poor Pressured but Great Clean', (90,22), fontsize=7, color = 'purple')

# Add a title
plt.title(f'PFF Clean Pocket Grade vs. PFF Under Pressure Grade', fontdict={'fontsize': 20})
plt.suptitle(f'Min. 5 Dropbacks')

# Style the chart
plt.show()
