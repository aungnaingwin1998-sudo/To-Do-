tasks = []

# ADD TASK 
def add_task():
    new_task = input("Enter the task you want to add: ").strip()

    if not new_task:
        print("Task cannot be empty.")
        return
    
    for t in tasks:
        if t["task"] == new_task:
            print(f"Task '{new_task}' already exists.")
            return

    tasks.append({"task": new_task, "Done": False})
    print(f"Task '{new_task}' added successfully.")


# VIEW TASK
def view_tasks():
    if not tasks:
        print("The task list is empty.")
    else:
        for i, k  in enumerate(tasks, start=1):
            if k["Done"] == True:
                status = "✓"
            else:
                status = "✗"
            print(f"{i}. {k['task']} [{status}]")


