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
        t = cls(
            data["description"],
            data["amount"],
            data["category"]
        )
        t.date = data.get("date", datetime.now().isoformat())
        return t

    def __str__(self):
        return (
            f"{self.description}: "
            f"${self.amount:.2f} "
            f"[{self.category}] "
            f"({self.date[:10]})"
        )


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
        return [
            t for t in self.transactions
            if t.category.lower() == category.lower()
        ]

    def filter(self, **filters):
        result = self.transactions.copy()

        if "category" in filters:
            cat = filters["category"].lower()
            result = [
                t for t in result
                if t.category.lower() == cat
            ]

        if "amount_min" in filters:
            result = [
                t for t in result
                if t.amount >= filters["amount_min"]
            ]

        return result

    def save(self, filename="transactions.json"):
        try:
            with open(filename, "w") as f:
                data = [t.to_dict() for t in self.transactions]
                json.dump(data, f, indent=2)

            print(f"\nSaved {len(self.transactions)} transactions.")

        except IOError as e:
            print(f"Error saving: {e}")

    def load(self, filename="transactions.json"):
        if not os.path.exists(filename):
            print("\nNo saved transactions found.")
            return

        try:
            with open(filename, "r") as f:
                data = json.load(f)

            self.transactions = [
                Transaction.from_dict(item)
                for item in data
            ]

            print(f"\nLoaded {len(self.transactions)} transactions.")

        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading: {e}")
            self.transactions = []


def main():
    tracker = FinanceTracker()
    tracker.load()

    print("\n=== Personal Finance Tracker (OOP) ===")

    while True:
        print("\n1. Add Transaction")
        print("2. Get Balance")
        print("3. Get By Category")
        print("4. Filter Transactions")
        print("5. View All Transactions")
        print("6. Save & Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            desc = input("Description: ")

            try:
                amt = float(input("Amount: "))
            except ValueError:
                print("Invalid amount.")
                continue

            cat = input("Category: ")

            tracker.add(desc, amt, cat)
            print("Transaction added successfully.")

        elif choice == "2":
            print(f"\nCurrent Balance: ${tracker.get_balance():.2f}")

        elif choice == "3":
            cat = input("Enter category: ")

            results = tracker.get_by_category(cat)

            if not results:
                print("No transactions found.")
            else:
                print("\nTransactions:")
                for t in results:
                    print(t)

        elif choice == "4":
            cat = input(
                "Category (leave blank to skip): "
            ).strip()

            min_amt = input(
                "Minimum amount (leave blank to skip): "
            ).strip()

            filters = {}

            if cat:
                filters["category"] = cat

            if min_amt:
                try:
                    filters["amount_min"] = float(min_amt)
                except ValueError:
                    print("Invalid amount.")
                    continue

            results = tracker.filter(**filters)

            if not results:
                print("No matching transactions.")
            else:
                print("\nFiltered Transactions:")
                for t in results:
                    print(t)

        elif choice == "5":
            if not tracker.transactions:
                print("No transactions available.")
            else:
                print("\nAll Transactions:")
                for i, t in enumerate(tracker.transactions, start=1):
                    print(f"{i}. {t}")

        elif choice == "6":
            tracker.save()
            print("Thank you for using Finance Tracker!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()