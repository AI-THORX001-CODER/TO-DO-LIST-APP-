import time

tasks = []


def show_tasks():
    if not tasks:
        print(" No tasks available.")
    else:
        print(" Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = " Done" if task["done"] else "⏳ Pending"
            print(f"{i}. {task['name']} - {status}")


def add_task():
    name = input("Enter new task: ")
    tasks.append({"name": name, "done": False})
    print(" Task added successfully!")


def start_task():
    show_tasks()
    if not tasks:
        return

    try:
        num = int(input("Enter task number to start: "))
        if 1 <= num <= len(tasks):
            print(f"⏱️ Starting task: {tasks[num - 1]['name']}")
            time.sleep(1)
            print("▶ bring it on")
        else:
            print("system crash")
    except ValueError:
        print(" Please enter a valid number")


def finish_task():
    show_tasks()
    if not tasks:
        return

    try:
        num = int(input("Enter task number to finish: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print(" you got it")
        else:
            print(" system crash")
    except ValueError:
        print(" Please enter a valid number")


def delete_task():
    show_tasks()
    if not tasks:
        return

    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f" Task '{removed['name']}' deleted")
        else:
            print(" system crash")
    except ValueError:
        print(" Please enter a valid number")


def todo_app():
    while True:
        print("\n---  To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Start Task")
        print("4. Finish Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_task()

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            start_task()

        elif choice == "4":
            finish_task()

        elif choice == "5":
            delete_task()

        elif choice == "6":
            print( "sytem exit ")
            break

        else:
            print(" Invalid choice. Try again!")


todo_app()
