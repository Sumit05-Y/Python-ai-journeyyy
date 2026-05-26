n = int(input("Enter no of items: "))

name = []
price = []

for i in range(n):
    item_name = input("Enter item name: ")
    item_price = float(input("Enter item price: "))

    name.append(item_name)
    price.append(item_price)

print("------ RECEIPT ------")

print(f'{"ITEM NAME":<15} {"ITEM PRICE":>10}')

for i, j in zip(name, price):
    print(f'{i:<15} {j:>10.2f}')

sub_total = sum(price)

print("------ TOTAL ------")

print(f"Sub total  : {sub_total:.2f}")

tax_amount = sub_total * 0.15
print(f"Tax amount : {tax_amount:.2f}")

total = sub_total + tax_amount
print(f"Total amount : {total:.2f}")


