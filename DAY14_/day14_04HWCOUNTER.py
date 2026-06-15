def counter_factory():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    print(count)
    return counter
choice = input("Enter \n 1. for increment \n 2. for exit ")

if choice == "1":
    counter_factory()

