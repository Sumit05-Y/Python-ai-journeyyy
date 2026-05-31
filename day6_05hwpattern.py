def right_triangle(n):
    for i in range(1,n+1):
        print("* " * i)
def inverted_pattern(n):
    for i in range(n,0,-1):
        print("* " * i)
def pyramid_pattern(n):
    for i in range(1,n+1):
        sp=" " * (n - i)
        print(sp + "* " * i)

try:
    user_choice=int(input("Enter \n1)for right traingle pattern:\n2)for inverted pattern:\n3)for pyramid pattern:\n"))
    try:
        n=int(input("Enter the size of pattern:"))
    except ValueError:
        print(f"Invalid option")
    if user_choice == 1:
        right_triangle(n)
    elif user_choice == 2:
        inverted_pattern(n)
    elif user_choice == 3:
        pyramid_pattern(n)
    else:
        print(f"Invalid option")
except ValueError:
    print(f"Invalid option")
