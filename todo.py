tasks = []

def show_menu():
    print("\nTodo List")
    print("1. Add task")
    print("2. Delete task")
    print("3. Task completed")
    print("4. View tasks")
    print("5. Exit")

def add_task():
    task = input("Task description: ")
    tasks.append({"task": task, "completed": False})
    print("Task added")

def delete_task():
    view_tasks()
    task_index = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        print("Task deleted")
    else:
        print("Invalid number.")

def mark_completed():
    view_tasks()
    task_index = int(input("Enter task number completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task completed")
    else:
        print("Invalid number.")

def view_tasks():
    if not tasks:
        print("No tasks")
    else:
        print("\n Tasks:")
        for i, task in enumerate(tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{i + 1}. {task['task']} - [{status}]")

while True:
    show_menu()
    choice = input("Enter number: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        delete_task()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        view_tasks()
    elif choice == "5":
        print("Exit")
        break
    else:
        print("Invalid number. Try again.")
