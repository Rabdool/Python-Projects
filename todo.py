import os

TODO_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("📭 No tasks yet.")
    else:
        print("📝 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def todo_app():
    tasks = load_tasks()

    print("✅ Welcome to CLI To-Do List!")
    while True:
        print("\nOptions: [a]dd  [v]iew  [d]elete  [q]uit")
        choice = input("Choose an option: ").lower()

        if choice == 'a':
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")

        elif choice == 'v':
            show_tasks(tasks)

        elif choice == 'd':
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Enter a valid number.")

        elif choice == 'q':
            print("👋 Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    todo_app()
