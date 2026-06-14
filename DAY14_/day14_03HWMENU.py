menu = {
    "Drinks": {
        "Coffee": 150,
        "Tea": 100
    },
    "Food": {
        "Burger": 250,
        "Pizza": 500
    }
}

order = []


def add_item(item_name):
    for category in menu:
        if item_name in menu[category]:
            order.append({
                "item": item_name,
                "price": menu[category][item_name]
            })
            print(f"{item_name} added to your order.")
            return

    print("Item not found in the menu.")


def view_menu():
    for category in menu:
        print(f"\n{category}")
        for item, price in menu[category].items():
            print(f"{item} - Rs.{price}")


def view_order():
    if not order:
        print("No items ordered yet.")
        return

    total = 0
    print("\nYour Order:")
    for item in order:
        print(f"{item['item']} - Rs.{item['price']}")
        total += item["price"]

    print(f"Total = Rs.{total}")


def calculate_order():
    total = sum(item["price"] for item in order)
    return total


def filter_by_price(price_limit):
    filtered = {}

    for category in menu:
        filtered[category] = {}

        for item, price in menu[category].items():
            if price <= price_limit:
                filtered[category][item] = price

    return filtered


while True:
    print("\n===== MENU =====")
    print("1. View Menu")
    print("2. Add Item to Order")
    print("3. View Order")
    print("4. Calculate Total")
    print("5. Filter By Price")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_menu()

    elif choice == "2":
        item = input("Enter item name: ")
        add_item(item)

    elif choice == "3":
        view_order()

    elif choice == "4":
        print(f"Total = Rs.{calculate_order()}")

    elif choice == "5":
        limit = int(input("Enter maximum price: "))
        filtered = filter_by_price(limit)

        print("\nItems within your budget:")
        for category in filtered:
            if filtered[category]:
                print(f"\n{category}")
                for item, price in filtered[category].items():
                    print(f"{item} - Rs.{price}")

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
        