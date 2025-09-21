task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is high priority task that requires immediate attention today!.")
        else:
            print(f"Reminder: '{task}' needs your attention soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' a medium-priority task is time-bound. Try to complete it on time.")
        else:
            print(f"Reminder: '{task}' a medium-priority task is pending. Please schedule it accordingly.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' a low-priority task is time-bound. Don't forget to do it when you can.")
        else:
            print(f"Reminder: '{task}' a low-priority task can be done at your convenience.")
    case _:
        print("Invalid priority level. Please choose from high, medium, or low.")
