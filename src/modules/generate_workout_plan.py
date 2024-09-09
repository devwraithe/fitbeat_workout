import random

from src.modules.save_workout_plan import save_workout
from src.utilities.database import exercises


def check_file_exists():
    try:
        with open("workout.json", "r", encoding="utf-8") :
            return True
    except FileNotFoundError:
        return False


def get_diff_int(fitness_level):
    if fitness_level == "beginner":
        return 1
    elif fitness_level == "intermediate":
        return 2
    elif fitness_level == "advanced":
        return 3
    else:
        print("Invalid fitness level")
        return 0


def generate_workout(fitness_level):
    difficulty = get_diff_int(fitness_level)
    selected_exercises = []

    for exercise in random.sample(exercises, len(exercises)):
        if exercise['difficulty'] == difficulty:
            if len(selected_exercises) < 5:
                selected_exercises.append(exercise)

    save_workout(selected_exercises)

    print(f"\n{fitness_level.capitalize()} level exercises created just for you:")

    for selected_exercise in selected_exercises:
        print(f"- {selected_exercise['name']}")
