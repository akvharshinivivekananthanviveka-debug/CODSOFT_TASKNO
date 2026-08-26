tasks = []
while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully!")
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)
    elif choice == "3":
        number = int(input("Enter task number to update: "))
        if 1 <= number <= len(tasks):
            new_task = input("Enter new task: ")
            tasks[number - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    elif choice == "4":
        number = int(input("Enter task number to delete: "))
        if 1 <= number <= len(tasks):
            deleted_task = tasks.pop(number - 1)
            print("Deleted:", deleted_task)
        else:
            print("Invalid task number.")
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")