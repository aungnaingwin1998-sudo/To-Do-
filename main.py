tasks = [{"task": "Buy groceries", "Done": False}]

# ADD TASK 
def add_task():
    new_task = input("Enter the task you want to add: ").strip()

    if not new_task:
        print("Task cannot be empty.")
        return
    
    for t in tasks:
        if t["task"].lower() == new_task.lower():   # FIX (case-insensitive)
            print(f"Task '{new_task}' already exists.")
            return

    tasks.append({"task": new_task, "Done": False})
    print(f"Task '{new_task}' added successfully.")


# VIEW TASK
def view_tasks():
    if not tasks:
        print("The task list is empty.")
    else:
        for i, k in enumerate(tasks, start=1):
            if k["Done"] == True:
                status = "✓"
            else:
                status = "✗"
            print(f"{i}. {k['task'].title()} [{status}]")


# DELETE TASK
def delete_task():
    task_name = input("Enter the task you want to delete: ").strip().lower()
    
    for t in tasks:
        if t["task"].lower() == task_name:   # FIX (case-insensitive)
            tasks.remove(t)
            print(f"Task '{t['task'].title()}' deleted successfully.")
            return

    print(f"Task '{task_name}' not found.")

def update_status():
    task_update = input("Enter the task you want to update the status for: ").strip().lower()
    
    if not task_update:
        print("Task cannot be empty.")
        return

    update_status = input("Enter the new status (Done/Not Done): ").strip().lower()

    if update_status not in ["done", "not done"]:
        print("Invalid status. Please enter 'Done' or 'Not Done'.")
        return

    for t in tasks:
        if t["task"].lower() == task_update:
            if update_status == "done":
                t["Done"] = True
            else:
                t["Done"] = False

            print(f"Task '{t['task'].title()}' updated successfully.")
            return

    print(f"Task '{task_update}' not found.")