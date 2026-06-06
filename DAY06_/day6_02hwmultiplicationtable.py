#Print a complete 12×12 multiplication table as a formatted grid
#Each number right-aligned in 4 characters (use :>4 f-string).
#Use nested for loops throughout.

for i in range(1,13):
    print(f"12 x {i} = {12 * i :>4}")
