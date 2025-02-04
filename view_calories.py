def view_calories():
    with open('calorie_tracker.txt', 'r') as file:
        calories = file.read()
        print(calories)
