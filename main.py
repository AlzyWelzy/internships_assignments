from algorithm_1 import main as algorithm_1
from algorithm_3 import main as algorithm_3
from random_data import main as random_data


class MainProgram:
    def __init__(self):
        # Define program descriptions
        self.program_descriptions = {
            "1": "Algorithm 1: Calculates target variables",
            "2": "Algorithm 3: LSTM for student academic performance evaluation",
            "3": "Random Data: Generates random student performance data and saves to CSV",
        }

    def get_program_choice(self):
        # Print program descriptions and prompt user to choose a program
        print("Please choose a program to run:")
        for key, value in self.program_descriptions.items():
            print(f"{key}: {value}")
        program_choice = input("> ")
        return program_choice

    def run_program(self, program_choice):
        # Run the program based on user's choice
        if program_choice == "1":
            algorithm_1()
        elif program_choice == "2":
            algorithm_3()
        elif program_choice == "3":
            random_data()
        else:
            print("Invalid choice. Please try again.")

    def run(self):
        # Runs the program by getting user input and running selected program
        program_choice = self.get_program_choice()
        self.run_program(program_choice)


if __name__ == "__main__":
    main_program = MainProgram()
    main_program.run()
