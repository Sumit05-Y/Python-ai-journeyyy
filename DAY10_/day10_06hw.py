inventory = [
    ("Rice", 10, 100),
    ("Daal", 3, 150),
    ("Oil", 7, 200)
]

def add_item(name, qty, price):
    inventory.append((name, qty, price))
    for item in inventory:
        print(item)
    return
    

def update_quantity(name, new_qty):
    for i in range(len(inventory)):
        if inventory[i][0] == name:
            inventory[i] = (name, new_qty, inventory[i][2])

def total_value():
    total = 0
    for item in inventory:
        total += item[1] * item[2]
    return total

def low_stock_alert():
    for item in inventory:
        if item[1] < 5:
            print(item[0], "is low in stock")

def sort_by_price():
    print(sorted(inventory, key=lambda x: x[2]))

def sort_by_quantity():
    print(sorted(inventory, key=lambda x: x[1]))

print("-------Inventory------------")
for item in inventory:
    print(item)
print("------------------------------------")

print("1. ADD ITEM")
print("2. UPDATE QUANTITY")
print("3. TOTAL VALUE")
print("4. CHECK IS STOCK LOW")
print("5. SORT BY PRICE")
print("5. SORT BY QUANTITY")
choice = int(input("Enter choice 1-5 : "))

if choice == 1:

    while True:
        name = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        price = int(input("Enter price: "))

        add_item(name, qty, price)

        choice = input("Add another item? (y/n): ")
        if choice.lower() != "y":
            break
if choice == 2:
    item_name = input("\nEnter item name to update quantity: ")
    new_qty = int(input("Enter new quantity: "))
    update_quantity(item_name, new_qty)

if choice == 3:
    print("\nTotal Value:", total_value())

if choice == 4:
    print("\nLow Stock:")
    low_stock_alert()

if choice == 5:
    print("\nSorted by Price:")
    sort_by_price()

if choice == 6:
    print("\nSorted by Quantity:")
    sort_by_quantity()