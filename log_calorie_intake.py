def log_calorie_intake():
    food = input("Enter food: ")
    consumed_calories = input("Enter consumed calories: ")

    with open("calorie_tracker.txt", "a") as file:
        file.write(f"{food}, {consumed_calories}\n")

    total_calories = 0
    with open("calorie_tracker.txt", "r") as file:
        for line in file:
            entered_food, entered_consumed_calories = line.strip().split(", ")
            total_calories += int(entered_consumed_calories)

    print(f"Logged calories: {food}, calories: {consumed_calories}")
    print(f"Total calories: {total_calories}")

