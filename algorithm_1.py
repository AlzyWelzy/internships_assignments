# Assign values to variables
a = 80
b = 75
c = 85
d = 70
e = 90
f = 80
g = 80
h = True
i = True
j = True
semester_grades = [a, b, c, d, e, f]

# Calculate dropout
dropout = 1 if min(semester_grades) < 35 and g < 30 else 0

# Calculate good performance
good_performance = 1 if all(grade > 60 for grade in semester_grades) else 0

# Calculate poor performance
poor_performance = 1 if max(semester_grades) < 40 else 0

# Calculate support required
support_required = 1 if any(40 <= grade < 60 for grade in semester_grades) else 0

# Calculate eligibility for placement
eligible_for_placement = 1 if all(grade > 65 for grade in semester_grades) and (j or i or h) else 0

# Print the results
print("Dropout:", dropout)
print("Good performance:", good_performance)
print("Poor performance:", poor_performance)
print("Support required:", support_required)
print("Eligible for placement:", eligible_for_placement)
