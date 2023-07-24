import csv
import pandas as pd
import matplotlib.pyplot as plt

# Import Pressure CSV file
pressure_data = "CFF_PFF_pressure_grades.csv"

# Open CSV file and read data
with open(pressure_data, 'r', newline='') as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip the header row
    data = []

    # Loop through data
    for row in reader:
        name = row[0]
        pressure_grade_str = row[4]
        clean_grade_str = row[5]
        num_dropbacks = int(row[7])

         # Add validation for minimum number of dropbacks
        if num_dropbacks >= 200:
            pressure_grade = float(pressure_grade_str)
            clean_grade = float(clean_grade_str)
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

# Find grade averages for pressured and un-pressured league-wide
clean_avg = xy['x'].mean()
pressure_avg = xy['y'].mean()

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
plt.xlim((40, 100))
plt.ylim((20, 100))

# Add labels for axes
plt.xlabel('Clean PFF Grade', size=6, color='green')
plt.ylabel('Under Pressure PFF Grade', size=6, color='red')

# Annotate with QB name and year
for i in xy.index:
    plt.annotate(f"{xy['name'][i]}", (xy['x'][i] + .35, xy['y'][i] + .5), fontsize=5)

plt.annotate('Great Clean and Pressured', (90, 90), fontsize=7, color='green')
plt.annotate('Great Pressured but not Clean?', (40, 90), fontsize=7, color='purple')
plt.annotate('Poor Clean and Pressured', (40, 30), fontsize=7, color='red')
plt.annotate('Poor Pressured but Great Clean', (90, 30), fontsize=7, color='purple')

# Add a title
plt.suptitle(f' 2022 College PFF Clean Pocket Grade vs. PFF Under Pressure Grade', fontsize=15)
plt.title(f'Min. 200 Dropbacks \nLeague Averages: Clean Pocket Avg. ({clean_avg:.2f}), Pressured Avg. ({pressure_avg:.2f})', fontsize=7, loc = 'left')

# Style the chart
plt.tight_layout()  # Improves layout of the plot
plt.show()