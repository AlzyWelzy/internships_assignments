import numpy as np
import pandas as pd

# Generate random data for student_performance.csv
num_students = 100
df = pd.DataFrame(
    {
        "id": np.arange(num_students),
        "gender": np.random.choice(["M", "F"], size=num_students),
        "age": np.random.randint(18, 25, size=num_students),
        "1-1_percentage": np.random.randint(0, 101, size=num_students),
        "1-2_percentage": np.random.randint(0, 101, size=num_students),
        "2-1_percentage": np.random.randint(0, 101, size=num_students),
        "2-2_percentage": np.random.randint(0, 101, size=num_students),
        "3-1_percentage": np.random.randint(0, 101, size=num_students),
        "3-2_percentage": np.random.randint(0, 101, size=num_students),
        "coding_skills": np.random.choice([0, 1], size=num_students),
        "academic_awards": np.random.choice([0, 1], size=num_students),
        "extracurricular_activities": np.random.choice([0, 1], size=num_students),
    }
)

# Save the dataset to student_performance.csv
df.to_csv("student_performance.csv", index=False)
