import json


def save_workout(workout):
    with open("workout.json", "w", encoding="utf-8") as f:
        json.dump(workout, f, ensure_ascii=False, indent=4)