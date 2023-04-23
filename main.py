import algorithm_1
import algorithm_2
import random_data

from algorithm_1 import main as algorithm_1
from algorithm_2 import main as algorithm_2
from random_data import main as random_data


class MainProgram:
    def __init__(self):
        # Define program descriptions
        self.program_descriptions = {
            "1": "Algorithm 1: Evaluates student performance based on semester grades",
            "2": "Algorithm 3: Predicts customer churn using machine learning",
            "3": "Random Data: Generates random student performance data and saves to CSV",
        }

    def choice(self):
        # Print program descriptions and prompt user to choose a program
        print("Please choose a program to run:")
        for key, value in self.program_descriptions.items():
            print(f"{key}: {value}")
        program_choice = input("> ")
        return program_choice

    def run(self):
        # Run the program
        program_choice = self.choice()
        if program_choice == "1":
            algorithm_1()
        elif program_choice == "2":
            algorithm_2()
        elif program_choice == "3":
            random_data()
        else:
            print("Invalid choice. Please try again.")
            self.run()


def main():
    # Run the program
    main_program = MainProgram()
    main_program.run()


if __name__ == "__main__":
    main()
