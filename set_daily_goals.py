def set_daily_goals():
    """
    daily_time_workout - how long should the daily workout be?
    daily_calorie_intake - what should be the calorie goal for the day?
    :return:
    """
    daily_time_workout = input("Enter workout goal: ")
    daily_calorie_intake = input("Enter daily calorie limit: ")

    with open("daily_goals.txt", "a") as file:
        file.write(f"Daily workout goal: {daily_time_workout}\nDaily calorie limit: {daily_calorie_intake}\n")

    print(f"Daily workout duration is set to {daily_time_workout} and the daily calorie limit is set to {daily_calorie_intake}")