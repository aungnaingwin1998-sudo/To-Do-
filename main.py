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