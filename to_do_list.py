import json

class ToDoList:
    def __init__(self, filename='todo.json'):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        self.save_tasks()

    def update_task(self, task_number, new_task):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]['task'] = new_task
            self.save_tasks()
        else:
            print("Invalid task number")

    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            del self.tasks[task_number]
            self.save_tasks()
        else:
            print("Invalid task number")

    def mark_done(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]['done'] = True
            self.save_tasks()
        else:
            print("Invalid task number")

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "Done" if task['done'] else "Not Done"
            print(f"{i}. {task['task']} - {status}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Mark task as done")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_number, new_task)
        elif choice == '4':
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to mark as done: "))
            todo_list.mark_done(task_number)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

