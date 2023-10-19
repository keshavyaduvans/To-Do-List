class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the list.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def update_task(self, task_index, new_task):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1] = new_task
            print(f"Task {task_index} updated to '{new_task}'.")
        else:
            print("Invalid task index. Please try again.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task {task_index} ('{removed_task}') removed from the list.")
        else:
            print("Invalid task index. Please try again.")

def main():
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Remove Task")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks()
            task_index = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_index, new_task)
        elif choice == "4":
            todo_list.view_tasks()
            task_index = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
