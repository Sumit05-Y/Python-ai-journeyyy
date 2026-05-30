#balance = 1000. while menu: 
#1) Check balance  2) Deposit  3) Withdraw  4) Exit.
#Handle invalid amounts: can't withdraw more than balance
#can't deposit negative.
def check_balance(balance):
      print(f"Balance = {balance}")
      return balance
def deposit_balance(balance):
    add_balance=float(input("enter amount to be deposited:\n"))
    if add_balance < 0:
           print(f"Invalid amount")
    else:
        balance += add_balance
    return balance
def withdraw_balance(balance):
    remove_balance=float(input("enter amount to be withdraw:\n"))
    if remove_balance > balance:
        print(f"Not enough amount")
    elif remove_balance < 0:
        print(f"invalid option")
    else:
        balance -= remove_balance
    return balance
      
    
    
    
    
balance = 1000 
    
print(f"---------ATM---------")
options = input("Enter menu: ")
while options.lower() == "menu":
    try:
        user_choice=int(input("enter:\n 1) to Check balance\n 2) to Deposit money\n 3) to withdraw money\n 4) to exit\n"))
        if user_choice == 1:
            check_balance(balance)
        elif user_choice == 2:
            balance = deposit_balance(balance)
        elif user_choice == 3:
            balance = withdraw_balance(balance)
        elif user_choice ==4:
            print(f"Thankyou for using ATM")
            break
        else:
            print("Invalid choice")
    except ValueError:
        print(f"Invalid choice")
print(f"--------------------------------------")

