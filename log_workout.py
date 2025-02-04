def log_workout() -> str:
    workout_type = input("Enter workout type: ")
    workout_duration = input("Enter workout duration: ")

    with open("fitness_tracker.txt", "a") as file:
        file.write(f"Workout: {workout_type}\nDuration: {workout_duration}\n")

    print(f"Logged workout: {workout_type}\nDuration: {workout_duration}\n")
