from src.modules.generate_workout_plan import generate_workout, check_file_exists
from src.modules.load_workout_plan import load_workout_plan


def main():
    print("====================\n"
          "+++ FitBeat Workout Planner +++"
          "\n====================")

    print("Select a choice:\n1. Create a new workout plan\n2. Load an existing plan")
    choice = input("Your choice: ")

    if choice == "1":
        file_exists = check_file_exists()

        if file_exists:
            print("A workout plan already exists. Do you want to overwrite it? (y/n)")
            if input().lower() == "y":
                fl_string = "(Beginner, Intermediate, Advanced)"
                fitness_level = input(f"What is your current fitness level? {fl_string}: ")
                generate_workout(fitness_level.lower())
            else:
                print("Workout plan not overwritten.")
        # Get the user information

    elif choice == "2":
        workout_plan = load_workout_plan()
        for workout in workout_plan:
            print(f"{workout['name']} - {workout['difficulty']}")
    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
