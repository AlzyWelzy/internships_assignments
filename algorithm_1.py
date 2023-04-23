class SemesterGrades:
    def __init__(self, grades):
        self.grades = grades

    def get_min_grade(self):
        return min(self.grades)

    def get_max_grade(self):
        return max(self.grades)

    def has_dropout(self, g):
        return 1 if self.get_min_grade() < 35 and g < 30 else 0

    def has_good_performance(self):
        return 1 if all(grade > 60 for grade in self.grades) else 0

    def has_poor_performance(self):
        return 1 if self.get_max_grade() < 40 else 0

    def support_required(self):
        return 1 if any(40 <= grade < 60 for grade in self.grades) else 0

    def eligible_for_placement(self, h, i, j):
        return 1 if all(grade > 65 for grade in self.grades) and (j or i or h) else 0


def main():
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
    semester_grades = SemesterGrades([a, b, c, d, e, f])

    # Calculate dropout
    dropout = semester_grades.has_dropout(g)

    # Calculate good performance
    good_performance = semester_grades.has_good_performance()

    # Calculate poor performance
    poor_performance = semester_grades.has_poor_performance()

    # Calculate support required
    support_required = semester_grades.support_required()

    # Calculate eligibility for placement
    eligible_for_placement = semester_grades.eligible_for_placement(h, i, j)

    # Print the results
    print("Dropout:", dropout)
    print("Good performance:", good_performance)
    print("Poor performance:", poor_performance)
    print("Support required:", support_required)
    print("Eligible for placement:", eligible_for_placement)


if __name__ == "__main__":
    main()
