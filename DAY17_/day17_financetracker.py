from datetime import datetime
import json
import os

class Transaction:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category
        self.date = datetime.now().isoformat()

    def to_dict(self):
        return {
        "description": self.description,
        "amount": self.amount,
        "category": self.category,
        "date": self.date
        }
    
    
    @classmethod
    def from_dict(cls, data):
        t = cls(data["description"], data["amount"], data["category"])
        t.date = data.get("date", datetime.now().isoformat())
        return t
    
    def __str__(self):
        return f"{self.description}: ${self.amount:.2f} [{self.category}]"
    

class FinanceTracker:

    def __init__(self):
        self.transactions = []  

    def add(self, description, amount, category):
        t = Transaction(description, amount, category)
        self.transactions.append(t)
        return t
    
    def get_balance(self):
        return sum(t.amount for t in self.transactions)
    
    def get_by_category(self, category):
        return [t for t in self.transactions
                if t.category.lower() == category.lower()]
    
    def filter(self, **filters):
        result = self.transactions.copy()
        if 'category' in filters:
            cat = filters['category'].lower()
            result = [t for t in result if t.category.lower() == cat]
        if 'amount_min' in filters:
            result = [t for t in result if t.amount >= filters['amount_min']]
        return result



    def save(self, filename="transactions.json"):
        try:
            with open(filename, "w") as f:
                data = [t.to_dict() for t in self.transactions]
                json.dump(data, f, indent=2)
            print(f"  Saved {len(self.transactions)} transactions.")
        except IOError as e:
            print(f"  Error saving: {e}")

    def load(self, filename="transactions.json"):
        
        if not os.path.exists(filename):
            print(f"  No saved file. Starting fresh.")
            return
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.transactions = [Transaction.from_dict(d) for d in data]
            print(f"  Loaded {len(self.transactions)} transactions.")
        except (json.JSONDecodeError, IOError) as e:
            print(f"  Error loading: {e}")
            self.transactions = []
class User:
    user_count = 0  

    def __init__(self, name):
        self.name = name
        self.created_at = datetime.now().isoformat()
        User.user_count += 1

    def greet(self):
        return f"Hi, I'm {self.name}"

    def __str__(self):
        return f"User: {self.name}"
    
class Admin(User):

    def __init__(self, name):
        super().__init__(name)  
        self.role = "admin"

    def delete_all(self, tracker):
        count = len(tracker.transactions)
        tracker.transactions = []
        tracker.save()
        print(f"  {self.name} (admin) deleted {count} transactions.")

def main():
    print("\n  === Personal Finance Tracker (OOP) ===")

    user = User("Ali")
    admin = Admin("Sara")
    print(f"  {user.greet()}")
    print(f"  {admin.greet()} (Role: {admin.role})")

    tracker = FinanceTracker()
    tracker.load()

    try:
        tracker.add("Groceries", 45.50, "food")
        tracker.add("Gas", 60.00, "transport")
    except Exception as e:
        print(f"  Error adding transaction: {e}")

    tracker.save()

    print(f"\n  Users this session: {User.user_count}")


if __name__ == "__main__":
    main()
        