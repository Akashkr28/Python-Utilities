import os

TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if(os.path.exists(TASK_FILE)):
        with open(TASK_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                text, status = line.strip().rsplit("||", 1)
                tasks.append({"text": text, "done": status == "done"})
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, 'w', encoding='utf-8') as f:
        for task in tasks:
            status = "done" if task["done"] else "not_done"
            f.write(f"{task['text']} || {status}\n")

def display_tasks(tasks):
    if not tasks:
        print("You have no task")
    else:
        for i, task in enumerate(tasks, 1):
            checkbok = "✅" if task["done"] else " "
            print(f"{i}. [{checkbok}] {task['text']}")
    print()

def task_manager():
    tasks = load_tasks()

    while True:
        print("\n-------- Task Manager --------")
        print("1. Add Task")
        print("2. View tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        match choice:
            case "1":
                text = input("Enter your task: ").strip()
                if text:
                    tasks.append({"text": text, "done": False})
                    save_tasks(tasks)
                else:
                    print("Task cannot be empty")

            case "2":
                display_tasks(tasks)

            case "3":
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number: "))
                    if 1 <= num <= len(tasks):
                        tasks[num -1]["done"] = True
                        save_tasks(tasks)
                        print("Task marked as done")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Invalid input")

            case "4":
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number to delete: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num -1)
                        save_tasks(tasks)
                        print("Task removed {removerd['text']}")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Invalid input")

            case "5":
                print("Goodbye!")
                break

            case _:
                print("Invalid choice")

task_manager()