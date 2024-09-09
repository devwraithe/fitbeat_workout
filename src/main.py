from src.modules.generate_workout_plan import generate_workout
from src.modules.load_workout_plan import load_workout_plan


def main():
    print("====================\n"
          "+++ FitBeat Workout Planner +++"
          "\n====================")

    print("Select a choice:\n1. Create a new workout plan\n2. Load an existing plan")
    choice = input("Your choice: ")

    if choice == "1":
        # Get the user information
        fl_string = "(Beginner, Intermediate, Advanced)"
        fitness_level = input(f"What is your current fitness level? {fl_string}: ")
        generate_workout(fitness_level.lower())
    elif choice == "2":
        workout_plan = load_workout_plan()
        for workout in workout_plan:
            print(f"{workout['name']} - {workout['difficulty']}")
    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
