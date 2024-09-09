from src.modules.generate_workout_plan import generate_workout


def main():
    print("====================\n"
          "+++ FitBeat Workout Planner +++"
          "\n====================")

    # Get the user information
    fl_string = "(Beginner, Intermediate, Advanced)"
    fitness_level = input(f"1. What is your current fitness level? {fl_string}: ")

    generate_workout(fitness_level.lower())


if __name__ == "__main__":
    main()
