Vip = {"Ram", "Shyam", "Hari"}
Regular = {"Geeta", "Sita", "Shyam"}


def show_lists():
    print("\n----- GUEST LISTS -----")
    print(f"VIP Guests     : {Vip}")
    print(f"Regular Guests : {Regular}")
    print(f"Guests on both lists : {Vip & Regular}")
    print(f"All unique guests    : {Vip | Regular}")


def add_member():
    try:
        choice = int(input("\nEnter\n1. Add to VIP\n2. Add to Regular\nChoice: "))

        name = input("Enter guest name: ").strip()

        if choice == 1:
            Vip.add(name)
            print(f"{name} added to VIP list.")

        elif choice == 2:
            Regular.add(name)
            print(f"{name} added to Regular list.")

        else:
            print("Invalid choice.")
            return

        show_lists()

    except ValueError:
        print("Please enter a valid number.")


def remove_name():
    try:
        choice = int(input("\nEnter\n1. Remove from VIP\n2. Remove from Regular\nChoice: "))

        name = input("Enter guest name: ").strip()

        if choice == 1:
            Vip.discard(name)
            print(f"Removal operation completed for '{name}'.")

        elif choice == 2:
            Regular.discard(name)
            print(f"Removal operation completed for '{name}'.")

        else:
            print("Invalid choice.")
            return

        show_lists()

    except ValueError:
        print("Please enter a valid number.")


def check_membership():
    try:
        choice = int(input("\nEnter\n1. Search VIP\n2. Search Regular\nChoice: "))

        name = input("Enter guest name: ").strip()

        if choice == 1:
            if name in Vip:
                print(f"{name} FOUND in VIP list.")
            else:
                print(f"{name} NOT FOUND in VIP list.")

        elif choice == 2:
            if name in Regular:
                print(f"{name} FOUND in Regular list.")
            else:
                print(f"{name} NOT FOUND in Regular list.")

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")


show_lists()

choice = int(input(
    "\nGUEST MANAGEMENT SYSTEM\n"
    "1. Add Member\n"
    "2. Remove Member\n"
    "3. Check Membership\n"
    "Choice: "
))

if choice == 1:
    add_member()

elif choice == 2:
    remove_name()

elif choice == 3:
    check_membership()

else:
    print("Invalid option.")