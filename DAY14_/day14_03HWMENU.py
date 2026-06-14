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

def add_item(category, item, price):
    menu[category][item] = price

def view_menu():
    for category in menu:
        print("\n" + category)
        for item in menu[category]:
            print(item, "-", menu[category][item])

def calculate_order(items):
    total = 0

    for item in items:
        for category in menu:
            if item in menu[category]:
                total += menu[category][item]

    return total

def filter_by_price(price_limit):
    filtered = {}

    for category in menu:
        filtered[category] = {}

        for item in menu[category]:
            if menu[category][item] <= price_limit:
                filtered[category][item] = menu[category][item]

    return filtered


while True:
    print("\n1. View Menu")
    print("2. Add Item")
    print("3. Calculate Order")
    print("4. Filter By Price")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_menu()

    elif choice == "2":
        category = input("Enter category: ")
        item = input("Enter item name: ")
        price = int(input("Enter price: "))
        add_item(category, item, price)

    elif choice == "3":
        items = input("Enter items separated by comma: ").split(",")
        print("Total =", calculate_order(items))

    elif choice == "4":
        limit = int(input("Enter maximum price: "))
        print(filter_by_price(limit))

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")