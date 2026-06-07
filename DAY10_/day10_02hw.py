cart = []


def show_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n--------- YOUR CART ---------")
    total = 0

    for i, item in enumerate(cart, start=1):
        print(f"{i}. {item['name']:<15} ${item['price']:>6.2f}")
        total += item["price"]

    print("-" * 30)
    print(f"{'TOTAL':<15} ${total:>6.2f}")


def add_item():
    name = input("Enter item name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        price = float(input("Enter item price: "))
    except ValueError:
        print("Invalid price.")
        return

    cart.append({"name": name, "price": price})
    print(f"{name} added to cart.")


def remove_item():
    if not cart:
        print("Nothing to remove.")
        return

    show_cart()

    try:
        choice = int(input("\nEnter item number to remove: "))

        if 1 <= choice <= len(cart):
            removed = cart.pop(choice - 1)
            print(f"{removed['name']} removed from cart.")
        else:
            print("Invalid item number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    print("--------- SHOPPING CART ---------")

    while True:
        print("\n1. View Cart")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                show_cart()

            elif choice == 2:
                add_item()

            elif choice == 3:
                remove_item()

            elif choice == 4:
                print("Thank you for shopping!")
                break

            else:
                print("Invalid choice. Please enter 1-4.")

        except ValueError:
            print("Please enter a number.")


main()