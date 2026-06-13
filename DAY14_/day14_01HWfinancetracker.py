#ADD transactions
transactions=[]

def add_transactions(description,amount,category):
    transaction={
        "Description":description,
        "Amount":amount,
        "Category":category
    }
    transactions.append(transaction)
    print(f"{description} added, Amount :{amount}")

#VIEW
def view_transactions():
    total =0
    print("-"*28)
    print(f"{'S.No'}{'Item':>6}{'Amount':>12}")
    print("-"*28)
    for i,item in enumerate(transactions,1):
        print(f"{i}.{item['Description']:>8} {item['Amount']:>12}")
        total +=item["Amount"]
    print("-"*28)
    print(f"{'Total':>17}:{total}")


#BALANCE
def get_balance():
    return sum(item["Amount"] for item in transactions)


def get_by_category(category):
    return [item["Amount"] for item in transactions if item["Category"].lower()==category.lower()]


def category_summary():
    if transactions == None:
        print(f"No Transactions yet!")
        return
    by_cat={}
    for item in transactions:
        cat=item["Category"]
        by_cat[cat] = by_cat.get(cat,0) + item["Amount"]
    print(f"--------Spendings By Category--------------")
    for cat,total in sorted(by_cat.items()):
        print(f"{cat:>5}    Total:{total:.2f}")
    print("-"*48)


#filter
def filter_transactions(**filters):
    result = transactions.copy()

    if 'category' in filters:
        cat = filters['category'].lower()
        result = [t for t in result if t['Category'].lower() == cat]

    if 'amount_min' in filters:
        result = [t for t in result if t['Amount'] >= filters['amount_min']]

    if 'amount_max' in filters:
        result = [t for t in result if t['Amount'] <= filters['amount_max']]

    return result


#add multiple at once
def add_multiple(*transactions_data):
    for desc, amount, cat in transactions_data:
        add_transactions(desc, amount, cat)


#monthly summary
def get_monthly_summary():
    if not transactions:
        return

    total = get_balance()
    by_cat = {}

    for t in transactions:
        by_cat[t['Category']] = by_cat.get(t['Category'], 0) + t['Amount']

    print(f"\n  === Monthly Summary ===")
    print(f"  Total: ${total:.2f}    Transactions: {len(transactions)}")
    print("\n  By Category:")

    for cat in sorted(by_cat.keys()):
        pct = (by_cat[cat] / total * 100) if total > 0 else 0
        print(f"    {cat:<18} ${by_cat[cat]:>8.2f}  ({pct:>5.1f}%)")


#main menu
def main():
    """Main menu loop."""
    print("\n  === Personal Finance Tracker ===")

    while True:
        print("\n  1. Add  2. View all  3. By category  4. Balance")
        print("  5. Summary  6. Filter  7. Monthly  8. Exit")

        choice = input("\n  Choose: ").strip()

        if choice == "1":
            desc = input("  Description: ")
            try:
                amt = float(input("  Amount: $"))
                cat = input("  Category: ")
                add_transactions(desc, amt, cat)
            except ValueError:
                print("  Invalid amount.")

        elif choice == "2":
            view_transactions()

        elif choice == "3":
            print(get_by_category(input("  Category: ")))

        elif choice == "4":
            print(f"  ${get_balance():.2f}")

        elif choice == "5":
            category_summary()

        elif choice == "6":
            cat = input("  Category (leave blank to skip): ").strip()
            min_amt = input("  Minimum amount (leave blank to skip): ").strip()
            max_amt = input("  Maximum amount (leave blank to skip): ").strip()

            filters = {}

            if cat:
                filters["category"] = cat
            if min_amt:
                filters["amount_min"] = float(min_amt)
            if max_amt:
                filters["amount_max"] = float(max_amt)

            print(filter_transactions(**filters))

        elif choice == "7":
            get_monthly_summary()

        elif choice == "8":
            print("\n  Goodbye!")
            break

        else:
            print("  Invalid choice.")


main()