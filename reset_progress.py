def reset_progress():
    print("Warning: This will delete all your workout logs, calorie records, and daily goals. Are you sure you want to reset your progress? (yes/no)")
    answer = input("(yes/no): ")
    if answer.lower() == 'yes':
        for file_name in ["fitness_tracker.txt", "calorie_tracker.txt", "daily_goals.txt"]:
            with open(file_name, "w"):
                pass
    elif answer.lower() == 'no':
        return

