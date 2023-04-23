import random
import csv

# Define the number of students
num_students = 1000

# Define the minimum and maximum values for semester percentages
min_percent = 20
max_percent = 100

# Define the minimum and maximum values for attendance percentages
min_attendance = 50
max_attendance = 100

# Generate random student data
data = []
for i in range(num_students):
    sem1_percent = random.randint(min_percent, max_percent)
    sem2_percent = random.randint(min_percent, max_percent)
    sem3_percent = random.randint(min_percent, max_percent)
    sem4_percent = random.randint(min_percent, max_percent)
    attendance = random.randint(min_attendance, max_attendance)
    row = [sem1_percent, sem2_percent, sem3_percent, sem4_percent, attendance]
    data.append(row)

# Write the data to a CSV file
with open("student_performance.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(
        ["sem1_percent", "sem2_percent", "sem3_percent", "sem4_percent", "attendance"]
    )
    writer.writerows(data)
