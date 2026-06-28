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