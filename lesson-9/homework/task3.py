import json
import csv

def load_tasks(filename='tasks.json'):
    with open(filename, 'r') as f:
        return json.load(f)
def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as f:
        json.dump(tasks, f, indent=4)
def display_tasks(tasks):
    print(f"{'ID':<5} {'Task':<20} {'Completed':<10} {'Priority':<8}")
    for task in tasks:
        print(f"{task['id']:<5} {task['task']:<20} {task['completed']:<10} {task['priority']:<8}")
def compute_stats(tasks):
    total = len(tasks)
    completed = sum(task['completed'] for task in tasks)
    pending = total - completed
    avg_priority = sum(task['priority'] for task in tasks) / total if total else 0
    print("\n--- Task Statistics ---")
    print(f"Total tasks: {total}")
    print(f"Completed tasks: {completed}")
    print(f"Pending tasks: {pending}")
    print(f"Average priority: {avg_priority:.2f}")
def convert_to_csv(tasks, filename='tasks.csv'):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["id", "task", "completed", "priority"])
        writer.writeheader()
        writer.writerows(tasks)
    print(f"\nTasks written to {filename}")
    
if __name__ == "__main__":
    tasks = load_tasks()
    display_tasks(tasks)
    compute_stats(tasks)
    tasks[0]['completed'] = True
    save_tasks(tasks)
    
    convert_to_csv(tasks)
