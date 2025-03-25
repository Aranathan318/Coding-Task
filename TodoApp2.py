import json
import os

TODO_FILE = "todo_list.json"

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from a file if it exists and is valid."""
        if os.path.exists(TODO_FILE):
            try:
                with open(TODO_FILE, "r") as file:
                    data = file.read().strip()
                    self.tasks = json.loads(data) if data else []
            except json.JSONDecodeError:
                print("Error: Corrupt todo_list.json. Creating a new task list.")
                self.tasks = []

    def save_tasks(self):
        """Save tasks to a file."""
        with open(TODO_FILE, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        """Add a new task."""
        self.tasks.append({"task": task, "done": False})
        self.save_tasks()
        print(f"Added: {task}")

    def view_tasks(self):
        """View all tasks."""
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("\nYour To-Do List:\n")
            for index, task in enumerate(self.tasks, start=1):
                status = "[✓]" if task["done"] else "[ ]"
                print(f"{index}. {status} {task['task']}")

    def complete_task(self, index):
        """Mark a task as completed."""
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1]["done"] = True
            self.save_tasks()
            print(f"Marked task {index} as complete.")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        """Delete a task from the list."""
        if 0 < index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"Deleted: {removed_task['task']}")
        else:
            print("Invalid task number.")

def main():
    todo = ToDoList()

    while True:
        print("*" * 34)
        print("\n     To-Do List Menu:\n")
        print("     1. Add Task")
        print("     2. View Tasks")
        print("     3. Mark Task as Complete")
        print("     4. Delete Task")
        print("     5. Exit\n")
        print("*" * 34)
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            task = input("Enter task: ").strip()
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.view_tasks()
            try:
                index = int(input("Enter task number to mark complete: ").strip())
                todo.complete_task(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            todo.view_tasks()
            try:
                index = int(input("Enter task number to delete: ").strip())
                todo.delete_task(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "5":
            print("\nGoodbye!  Have a nice day!\n")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
