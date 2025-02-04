def view_workouts():
    with open("fitness_tracker.txt", "r") as file:
        content = file.read()
        print("Workout progress: ")
        print(content)
