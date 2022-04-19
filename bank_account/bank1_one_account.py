account_name = "Joe"
account_balance = 100
account_password = "secret"

while True:
    print()
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press w to make a withdrawl")
    print("Press s to show the account")
    print("Press q to quit")
    print()

    action = input("What do you want to do? ")
    action = action.lower()
    action = action[0]
    print()

    if action == "b":
        print("Get balance: ")
        user_password = input("Please enter the password: ")
        if user_password != account_password:
            print("Incorrect password")
        else:
            print(f"Your balance is: {account_balance}")
    elif action == "d":
        print("Deposit: ")
        user_deposit_amount = input("Please enter amount to deposit: ")
        user_deposit_amount = int(user_deposit_amount)
        user_password = input("Please enter the password: ")
        if user_deposit_amount < 0:
            print("You cannot deposit a negative amount!")
        elif user_password != account_password:
            print("Incorrect password")
        else:
            account_balance += user_deposit_amount
            print(f"Your new balance is: {account_balance}")
    elif action == "s":
        user_password = input("Please enter the password: ")
        if user_password != account_password:
            print("Incorrect password")
        else:
            print("Show: ")
            print(f"Name: {account_name}")
            print(f"Balance: {account_balance}")
            print(f"Password: {account_password}")
            print()
    elif action == "q":
        break
    elif action == "w":
        print("Withdraw:")
        user_withdrawl_amount = input("Please enter the amount to withdrawl: ")
        user_withdrawl_amount = int(user_withdrawl_amount)
        user_password = input("Please enter the password: ")
        if user_withdrawl_amount < 0:
            print("You cannot withdrawl a negative amount!")
        elif user_password != account_password:
            print("Incorrect password")
        elif user_withdrawl_amount > account_balance:
            print("You cannot withdrawl more than you have in your account.")
        else:
            account_balance -= user_withdrawl_amount
            print(f"Your new balance is: {account_balance}")
    print("Done")
