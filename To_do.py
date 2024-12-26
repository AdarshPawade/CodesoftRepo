class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully!")

    def mark_completed(self, task_id):
        if task_id < len(self.tasks):
            self.tasks[task_id]["completed"] = True
            print(f"Task {task_id} marked as completed!")
        else:
            print("Invalid task ID!")

    def update_task(self, task_id, new_task):
        if task_id < len(self.tasks):
            self.tasks[task_id]["task"] = new_task
            print(f"Task {task_id} updated!")
        else:
            print("Invalid task ID!")

    def remove_task(self, task_id):
        if task_id < len(self.tasks):
            removed_task = self.tasks.pop(task_id)
            print(f"Task '{removed_task['task']}' removed!")
        else:
            print("Invalid task ID!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            for idx, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx}. {task['task']} - {status}")

def main():
    todo_list = Todo()
    
    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. Mark Task Completed")
        print("3. Update Task")
        print("4. Remove Task")
        print("5. View Tasks")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_id = int(input("Enter task ID to mark completed: "))
            todo_list.mark_completed(task_id)
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            new_task = input("Enter new task details: ")
            todo_list.update_task(task_id, new_task)
        elif choice == "4":
            task_id = int(input("Enter task ID to remove: "))
            todo_list.remove_task(task_id)
        elif choice == "5":
            todo_list.view_tasks()
        elif choice == "6":
            print("Exiting the application...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
