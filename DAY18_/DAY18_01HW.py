import json
import os
class Task:

    def __init__(self, title, description="", due_date="",
                 priority="Medium", status="Pending"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority   
        self.status = status        

    def mark_complete(self):
        self.status = "Complete"

    def to_dict(self):
        return {
            "title": self.title, "description": self.description,
            "due_date": self.due_date, "priority": self.priority,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data.get("description", ""),
                    data.get("due_date", ""), data.get("priority", "Medium"),
                    data.get("status", "Pending"))

    def __str__(self):
        marker = "✓" if self.status == "Complete" else " "
        return f"[{marker}] {self.title} (Due: {self.due_date or 'N/A'}) — {self.priority}"
    
class TaskManager:


    def __init__(self):
            self.tasks = []

    def add_task(self, title, description="", due_date="", priority="Medium"):
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)
        print(f"  Added: {task.title}")
        return task

    def view_all(self):
        if not self.tasks:
            print("\n  No tasks yet.")
            return
        print("\n  --- All Tasks ---")
        for i, task in enumerate(self.tasks, 1):
            print(f"  {i}. {task}")

    def view_by_status(self, status):
        filtered = [t for t in self.tasks if t.status.lower() == status.lower()]
        for i, task in enumerate(filtered, 1):
            print(f"  {i}. {task}")

    def view_by_priority(self, priority):
        filtered = [t for t in self.tasks if t.priority.lower() == priority.lower()]

        if not filtered:
            print("No tasks found.")
            return

        for i, task in enumerate(filtered, 1):
            print(f"{i}. {task}")

    def save(self, filename="tasks.json"):
        try:
            with open(filename, "w") as f:
                data = [t.to_dict() for t in self.tasks]
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"  Error saving tasks: {e}")

    def load(self, filename="tasks.json"):
        if not os.path.exists(filename):
            print("No saved tasks found. Starting fresh.")
            return
    
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]
            print(f"  Loaded {len(self.tasks)} tasks.")
        except (json.JSONDecodeError, IOError) as e:
            print(f"  Error loading tasks: {e}")
            self.tasks = []

    def mark_complete(self, index):
        try:
            self.tasks[index - 1].mark_complete()
            print(f"  Marked '{self.tasks[index - 1].title}' as complete.")
        except IndexError:
            print("  Invalid task number.")

    def delete_task(self, index):
        try:
            removed = self.tasks.pop(index - 1)
            print(f"  Deleted: {removed.title}")
        except IndexError:
            print("  Invalid task number.")

    def edit_task(self, index, new_title=None, new_due_date=None):
        try:
            task = self.tasks[index - 1]
            if new_title:
                task.title = new_title
            if new_due_date:
                task.due_date = new_due_date
            print(f"  Updated task: {task}")
        except IndexError:
            print("  Invalid task number.")
def main():
    print("\n  === Task Manager CLI ===")
    manager = TaskManager()
    manager.load()

    while True:
        print("\n  1. Add  2. View all  3. By status  4. By priority")
        print("  5. Complete  6. Delete  7. Edit   8. Exit")
        choice = input("\n  Choose: ").strip()

        if choice == "1":
            title = input("  Title: ").strip()
            if not title:
                print("  Title cannot be empty.")
                continue
            due = input("  Due date (YYYY-MM-DD): ").strip()
            priority = input("  Priority (default Medium): ").strip() or "Medium"
            manager.add_task(title, "", due, priority)
            manager.save()

        elif choice == "2":
            manager.view_all()

        elif choice == "3":
            status = input("  Enter status (Pending/Complete): ").strip()
            manager.view_by_status(status)

        elif choice == "4":
            priority = input("  Enter priority (High/Medium/Low): ").strip()
            manager.view_by_priority(priority)

        elif choice == "5":
            manager.view_all()
            try:
                idx = int(input("  Task number: "))
                manager.mark_complete(idx)
                manager.save()
            except ValueError:
                print("  Please enter a valid number.")

        elif choice == "6":
            manager.view_all()
            try:
                idx = int(input("  Task number: "))
                manager.delete_task(idx)
                manager.save()
            except ValueError:
                print("  Please enter a valid number.")

        elif choice == "7":
            manager.view_all()
            try:
                idx = int(input("  Task number: "))
                new_title = input("  New title (leave blank to keep same): ").strip()
                new_due = input("  New due date (leave blank to keep same): ").strip()
                manager.edit_task(
                    idx,
                    new_title if new_title else None,
                    new_due if new_due else None,
                )
                manager.save()
            except ValueError:
                print("  Please enter a valid number.")

        elif choice == "8":
            print("\n  Goodbye!")
            break

        else:
            print("  Invalid choice. Please try again.")


if __name__ == "__main__":
    main()