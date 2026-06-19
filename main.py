tasks = [{}]


# ADD TASK
def add_task():
    new_task = input("Enter the task you want to add: ").strip()

    if not new_task:
        print("Task cannot be empty.")
        return

    for t in tasks:
        if t["task"].lower() == new_task.lower():
            print(f"Task '{new_task}' already exists.")
            return

    tasks.append({"task": new_task, "Done": False})
    print(f"Task '{new_task}' added successfully.")


# VIEW TASKS
def view_tasks():
    if not tasks:
        print("The task list is empty.")
    else:
        for i, k in enumerate(tasks, start=1):
            status = "✓" if k["Done"] == True else "✗"
            print(f"{i}. {k['task'].title()} [{status}]")


# DELETE TASK
def delete_task():
    task_name = input("Enter the task you want to delete: ").strip().lower()

    if not task_name:
        print("Task cannot be empty.")
        return

    for t in tasks:
        if t["task"].lower() == task_name:
            tasks.remove(t)
            print(f"Task '{t['task'].title()}' deleted successfully.")
            return

    print(f"Task '{task_name}' not found.")


# UPDATE STATUS
def update_status():
    task_update = input("Enter the task you want to update: ").strip().lower()

    if not task_update:
        print("Task cannot be empty.")
        return

    status_input = input("Enter status (Done/Not Done): ").strip().lower()

    if status_input not in ["done", "not done"]:
        print("Invalid status. Please enter Done or Not Done.")
        return

    for t in tasks:
        if t["task"].lower() == task_update:
            if status_input == "done":
                t["Done"] = True
            else:
                t["Done"] = False

            print(f"Task '{t['task'].title()}' updated successfully.")
            return

    print(f"Task '{task_update}' not found.")


# MENU LOOP
while True:
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Update Task Status")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            update_status()
        elif choice == 5:
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")