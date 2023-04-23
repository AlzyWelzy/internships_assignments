import numpy as np
import pandas as pd

# Generate random data for the dataset
n_samples = 1000

student_id = np.arange(1, n_samples+1)
1_1_percentage = np.random.randint(20, 100, size=n_samples)
1_2_percentage = np.random.randint(20, 100, size=n_samples)
2_1_percentage = np.random.randint(20, 100, size=n_samples)
2_2_percentage = np.random.randint(20, 100, size=n_samples)
3_1_percentage = np.random.randint(20, 100, size=n_samples)
3_2_percentage = np.random.randint(20, 100, size=n_samples)
coding_skills = np.random.randint(0, 2, size=n_samples)
academic_awards = np.random.randint(0, 2, size=n_samples)
extracurricular_activities = np.random.randint(0, 2, size=n_samples)

# Create a dictionary for the data
data_dict = {'id': student_id,
             '1-1_percentage': 1_1_percentage,
             '1-2_percentage': 1_2_percentage,
             '2-1_percentage': 2_1_percentage,
             '2-2_percentage': 2_2_percentage,
             '3-1_percentage': 3_1_percentage,
             '3-2_percentage': 3_2_percentage,
             'coding_skills': coding_skills,
             'academic_awards': academic_awards,
             'extracurricular_activities': extracurricular_activities}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data_dict)

# Save the DataFrame to a CSV file
df.to_csv('student_performance.csv', index=False)
