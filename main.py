def show_tasks(tasks):
    if not tasks:
        print("\nTask list is empty")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

tasks = []

while True:
    print(">> To-Do List <<")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        show_tasks(tasks)

    elif choice == "2":
        new_task = input("\nEnter a new task:\n>> ").strip()
        if new_task:
            tasks.append(new_task)
            print("Task added!\n")
        else:
            print("Task cannot be empty!\n")

    elif choice == "3":
        show_tasks(tasks)
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed task: {removed}\n")
            else:
                print("\nInvalid task number!\n")
        except ValueError:
            print("Please enter a valid number!\n")

    elif choice == "4":
        print("Until next time")
        break

    else:
        print("Invalid selection, please choose 1-4.\n")
