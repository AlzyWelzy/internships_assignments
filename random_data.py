import random
import csv


class RandomStudentData:
    def __init__(
        self, num_students, min_percent, max_percent, min_attendance, max_attendance
    ):
        self.num_students = num_students
        self.min_percent = min_percent
        self.max_percent = max_percent
        self.min_attendance = min_attendance
        self.max_attendance = max_attendance

    def generate_data(self):
        # Generate random student data
        data = []
        for i in range(self.num_students):
            sem1_percent = random.randint(self.min_percent, self.max_percent)
            sem2_percent = random.randint(self.min_percent, self.max_percent)
            sem3_percent = random.randint(self.min_percent, self.max_percent)
            sem4_percent = random.randint(self.min_percent, self.max_percent)
            attendance = random.randint(self.min_attendance, self.max_attendance)
            row = [sem1_percent, sem2_percent, sem3_percent, sem4_percent, attendance]
            data.append(row)

        return data

    def save_to_csv(self, filename):
        # Write the data to a CSV file
        data = self.generate_data()
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "sem1_percent",
                    "sem2_percent",
                    "sem3_percent",
                    "sem4_percent",
                    "attendance",
                ]
            )
            writer.writerows(data)


def main():
    # Generate random student data and save to CSV
    random_student_data = RandomStudentData(100, 0, 100, 0, 100)
    random_student_data.save_to_csv("student_performance.csv")


if __name__ == "__main__":
    main()
