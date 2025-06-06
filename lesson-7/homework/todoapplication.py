class Task:
    def __init__ (self,task_id,title,description,due_date,status):
        self.task_id=task_id
        self.title=title
        self.description=description
        self.due_date=due_date
        self.status=status

    def to_csv(self):
        return f"{self.task_id},{self.title},{self.description},{self.due_date},{self.status}"
    def from_csv(line):
        parts=line.strip().split(",")
        if len(parts)!=5:
            return None
        return Task(parts[0],parts[1],parts[2],parts[3],parts[4])
    def to_json(self):
        return '{' + f'"task_id":"{self.task_id}","title":"{self.title}","description":"{self.description}","due_date":"{self.due_date}","status":"{self.status}"' + '}'


    def from_json(line):
        line.strip()[1:-1]
        parts=line.split(",")
        data={}
        for part in parts:
            if ':' in part:
                key, value = part.replace('"', '').split(':', 1)
                data[key] = value
        return Task(data["task_id"], data["title"], data["description"], data["due_date"], data["status"])
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    def update_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input("New Title: ")
                task.description = input("New Description: ")
                task.due_date = input("New Due Date: ")
                task.status = input("New Status: ")
                return True
        return False

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def filter_tasks(self, status):
        for task in self.tasks:
            if task.status.lower() == status.lower():
                print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    def save_tasks(self, filename, format_type):
        with open(filename, 'w') as f:
            for task in self.tasks:
                if format_type == 'csv':
                    f.write(task.to_csv() + '\n')
                elif format_type == 'json':
                    f.write(task.to_json() + '\n')

    def load_tasks(self, filename, format_type):
        self.tasks = []
        try:
            with open(filename, 'r') as f:
                for line in f:
                    if format_type == 'csv':
                        task = Task.from_csv(line)
                    elif format_type == 'json':
                        task = Task.from_json(line)
                    if task:
                        self.tasks.append(task)
        except FileNotFoundError:
            print("File not found. Starting with empty task list.")


def main():
    manager = TaskManager()
    file_format = input("Choose file format (csv/json): ").strip().lower()
    filename = input("Enter filename (e.g., tasks.txt): ").strip()

    manager.load_tasks(filename, file_format)

    while True:
        print("""
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit
""")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            task = Task(
                input("Enter Task ID: "),
                input("Enter Title: "),
                input("Enter Description: "),
                input("Enter Due Date (YYYY-MM-DD): "),
                input("Enter Status (Pending/In Progress/Completed): ")
            )
            manager.add_task(task)
            print("Task added successfully!")

        elif choice == '2':
            print("\nTasks:")
            manager.view_tasks()

        elif choice == '3':
            if manager.update_task(input("Enter Task ID to update: ")):
                print("Task updated.")
            else:
                print("Task not found.")

        elif choice == '4':
            manager.delete_task(input("Enter Task ID to delete: "))
            print("Task deleted.")

        elif choice == '5':
            manager.filter_tasks(input("Enter status to filter by (Pending/In Progress/Completed): "))

        elif choice == '6':
            manager.save_tasks(filename, file_format)
            print("Tasks saved to file.")

        elif choice == '7':
            manager.load_tasks(filename, file_format)
            print("Tasks loaded from file.")

        elif choice == '8':
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()