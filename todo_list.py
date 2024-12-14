
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    print("\nTo-Do List:")
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks available!")

def delete_task(index):
    try:
        removed = tasks.pop(index - 1)
        print(f"Task '{removed}' removed!")
    except IndexError:
        print("Invalid task number!")

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        try:
            task_num = int(input("Enter the task number to delete: "))
            delete_task(task_num)
        except ValueError:
            print("Invalid input!")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
