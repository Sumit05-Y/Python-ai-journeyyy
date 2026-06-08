cart = [
    {"name": "rice", "price": 100},
    {"name": "daal", "price": 200},
    {"name": "bhat", "price": 150},
    {"name": "bhat", "price": 150},{"name": "daal", "price": 200},]


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
def search_item():
    query=input("Enter the item to be searched:\n")
    query1=query.lower()
    result=[item for item in cart if query1 in item['name'].lower()]
    if result:
        print(f"{query} FOUNDED")
        for item in result:
            print(f"{item['name']:<15}{item['price']:>6.2f}")
    else:
        print(f"{query} NOT FOUND")
def duplicate_item():
    names=[item['name'].lower() for item in cart]
    seen = set()
    duplicate = set()
    for name in names:
        if name in seen:
            duplicate.add(name)
        seen.add(name)
    if duplicate:
        print(f"Duplicated item:\n{','.join(duplicate)}")
    else:
        print(f"No duplicate item.")

def sort_item(by="name"):
    if not cart:
        print(f"The cart is empty nothing to sort!")
    if by == "name":
        cart.sort(key = lambda item: item['name'].lower())
        print("ITEM SORTED BY NAME")
        show_cart()
    elif by == "price":
        cart.sort(key = lambda item : item['price'])
        print("ITEM SORTED BY PRICE")
        show_cart()
def stats_():
    if not cart:
        return
    prices=[item['price'] for item in cart]
    print(f"no of items: {len(cart)}")
    print(f"Total : {sum(prices):.2f}")
    print(f"Average : {sum(prices)/len(cart):.2f}")
    





def main():
    
    print("--------- SHOPPING CART ---------")

    while True:
        print("\n1. View Cart")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. TO SEARCH")
        print("5. DUPLICATE ITEM")
        print("6. SORT ITEM BY NAME")
        print("7. SORT ITEM BY PRICE")
        print("8. Statistics")
        print("9. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                show_cart()

            elif choice == 2:
                add_item()

            elif choice == 3:
                remove_item()

            elif choice == 4:
                search_item()

            elif choice == 5:
                duplicate_item()
            
            elif choice == 6:
                sort_item("name")
            elif choice == 7:
                sort_item("price")
            
            elif choice == 8:
                stats_()


            elif choice == 9:
                print("Thank you for shopping!")
                break

            else:
                print("Invalid choice. Please enter 1-4.")

        except ValueError:
            print("Please enter a number.")


main()