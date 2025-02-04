from log_workout import log_workout
from view_workouts import view_workouts
from log_calorie_intake import log_calorie_intake
from view_calories import view_calories
from set_daily_goals import set_daily_goals
from reset_progress import reset_progress


def main():
    """
    Main function to interact with the user.
    """
    print("Welcome to the Personal Fitness Tracker System 🏋️‍♂️\n")

    while True:
        # Display menu options
        print("1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Workouts")
        print("4. View Calorie Intake")
        print("5. Reset Progress")
        print("6. Set Daily Goals")
        print("7. Exit")

        # Prompt user for their choice
        choice = input("\nEnter your choice: ")

        if choice == '1':
            log_workout()

        elif choice == '2':
            log_calorie_intake()

        elif choice == '3':
            view_workouts()

        elif choice == '4':
            view_calories()

        elif choice == '5':
            reset_progress()

        elif choice == '6':
            set_daily_goals()

        elif choice == '7':
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            exit()
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()