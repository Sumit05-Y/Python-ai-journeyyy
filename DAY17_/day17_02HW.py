class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money!")
        else:
            self.balance = self.balance - amount
            print(f"Withdrew {amount}. New balance: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance = self.balance + interest
        print(f"Added interest: {interest}. New balance: {self.balance}")


class CheckingAccount(Account):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Cannot withdraw that much, even with overdraft!")
        else:
            self.balance = self.balance - amount
            print(f"Withdrew {amount}. New balance: {self.balance}")


def main():
    print("Welcome! Let's set up your account.")
    name = input("Enter your name: ")
    acc_type = input("Account type - type 's' for Savings or 'c' for Checking: ")

    if acc_type.lower() == "s":
        rate = float(input("Enter interest rate (e.g. 0.05 for 5%): "))
        account = SavingsAccount(name, 0, rate)
    else:
        limit = float(input("Enter overdraft limit: "))
        account = CheckingAccount(name, 0, limit)

    while True:
        print("\n----- MENU -----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        if isinstance(account, SavingsAccount):
            print("4. Add interest")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Amount to deposit: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Amount to withdraw: "))
            account.withdraw(amount)

        elif choice == "3":
            print(f"Current balance: {account.balance}")

        elif choice == "4" and isinstance(account, SavingsAccount):
            account.add_interest()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()