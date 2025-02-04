def view_calories():
    with open('calorie_tracker.txt', 'r') as file:
        calories = file.read()
        print(calories)

        total_calories = 0
        with open("calorie_tracker.txt", "r") as file:
            for line in file:
                entered_food, entered_consumed_calories = line.strip().split(", ")
                total_calories += int(entered_consumed_calories)
        print(f"Total calories: {total_calories}")