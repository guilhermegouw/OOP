account_name = ""
account_balance = 0
account_password = ""


def new_account(name, balance, password):
    global account_name, account_balance, account_password
    account_name = name
    account_balance = balance
    account_password = password


def show(password):
    global account_name, account_balance, account_password
    if password != account_password:
        print("Incorrect password")
        return None
    print()
    print(f"Name: {account_name}")
    print(f"Balance: {account_balance}")
    print(f"Password: {account_password}")
    print()


def get_balance(password):
    global account_name, account_balance, account_password
    if password != account_password:
        print("Incorrect password")
        return None
    return account_balance


def deposit(password, amount):
    global account_name, account_balance, account_password
    if password != account_password:
        print("Incorrect password")
        return None
    elif amount < 0:
        print("You can not deposit a negative amount.")
        return None
    account_balance += amount
    return account_balance


def withdrawl(password, amount):
    global account_name, account_balance, account_password
    if password != account_password:
        print("Incorrect password")
        return None
    elif amount < 0:
        print("You can not withdrawl a negative amount.")
        return None
    elif amount > account_balance:
        print("You can not withdrawl more than you have in your account.")
        return None
    account_balance -= amount
    return account_balance


new_account("Guilherme", 100, "secret")

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
        print("Get balance:")
        user_password = input("Enter the password: ")
        the_balance = get_balance(user_password)
        if the_balance is not None:
            print(f"Your balance is: {the_balance}")
    elif action == "d":
        print("Deposit:")
        user_password = input("Enter the password: ")
        amount = input("Enter the amount you want to deposit: ")
        amount = int(amount)
        new_balance = deposit(user_password, amount)
        if deposit is not None:
            print(f"Your balance is: {new_balance}")
    elif action == "w":
        print("Withdrawl:")
        user_password = input("Enter the password: ")
        amount = input("Enter the amount you want to withdrawl: ")
        amount = int(amount)
        new_balance = withdrawl(user_password, amount)
        if withdrawl is not None:
            print(f"Your balance is: {new_balance}")
    elif action == "s":
        user_password = input("Enter the password: ")
        show(user_password)
    elif action == "q":
        print("Bye")
        break
