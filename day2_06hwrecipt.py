#User enters 3 item names and prices.
#Calculate subtotal, 15% tax, and total
#Print a receipt with aligned columns 
#name left-aligned, price right-aligned. Use :<15 and :>10 format codes.

item1_name=input("Enter 1st item")
item1_price=float(input("Enter 1st item's price"))

item2_name=input("Enter 2nd item")
item2_price=float(input("Enter 2nd item's price"))

item3_name=input("Enter 3rd item")
item3_price=float(input("Enter 3rd item's price"))

sub_total=item1_price+item2_price+item3_price
tax_amount=sub_total * (15/100)
total_amount=sub_total + tax_amount

print("-------RECEIPT-------")
print(f"{"item":<15} {"price":>10}")
print(f"{item1_name:<15} {item1_price:>10}")
print(f"{item2_name:<15}{item2_price:>10}")
print(f"{item3_name:<15}{item3_price:>10}")
print("-------TOTAL-------")
print(f"{"sub total" :>15} {sub_total}")
print(f"{"tax amount":>15} {tax_amount}")
print(f"{"Total amount":>15} {total_amount}")

