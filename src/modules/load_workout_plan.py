import json


def load_workout_plan():
    with open("workout.json", "r", encoding="utf-8") as f:
        workout = json.load(f)
    return workout
