account_0_name = ""
account_0_balance = 0
account_0_password = ""
account_1_name = ""
account_1_balance = 0
account_1_password = ""
n_accounts = 0


def new_account(account_number, name, balance, password):
    global account_0_name, account_0_balance, account_0_password
    global account_1_name, account_1_balance, account_1_password

    if account_number == 0:
        account_0_name = name
        account_0_balance = balance
        account_0_password = password
    if account_number == 1:
        account_1_name = name
        account_1_balance = balance
        account_1_password = password


def show(account_number, password):
    global account_0_name, account_0_balance, account_0_password
    global account_1_name, account_1_balance, account_1_password

    if account_number == 0:
        if password != account_0_password:
            print("Incorrect password")
            return None
        if account_0_name != "":
            print("Account 0")
            print(f"Name: {account_0_name}")
            print(f"Balance: {account_0_balance}")
            print(f"Password: {account_0_password}")
            print()
    if account_number == 1:
        if password != account_1_password:
            print("Incorrect password")
            return None
        if account_1_name != "":
            print("Account 1")
            print(f"Name: {account_1_name}")
            print(f"Balance: {account_1_balance}")
            print(f"Password: {account_1_password}")
            print()


def get_balance(account_number, password):
    global account_0_name, account_0_balance, account_0_password
    global account_1_name, account_1_balance, account_1_password

    if account_number == 0:
        if password != account_0_password:
            print("Incorrect password")
            return None
        return account_0_balance
    if account_number == 1:
        if password != account_1_password:
            print("Incorrect password")
            return None
        return account_1_balance


def deposit(account_number, password, amount):
    global account_0_name, account_0_balance, account_0_password
    global account_1_name, account_1_balance, account_1_password
    if account_number == 0:
        if password != account_0_password:
            print("Incorrect password")
            return None
        elif amount < 0:
            print("You can not deposit a negative amount.")
            return None
        account_0_balance += amount
        return account_0_balance
    if account_number == 1:
        if password != account_1_password:
            print("Incorrect password")
            return None
        elif amount < 0:
            print("You can not deposit a negative amount.")
            return None
        account_1_balance += amount
        return account_1_balance


def withdrawl(account_number, password, amount):
    global account_0_name, account_0_balance, account_0_password
    global account_1_name, account_1_balance, account_1_password
    if account_number == 0:
        if password != account_0_password:
            print("Incorrect password")
            return None
        elif amount < 0:
            print("You can not withdrawl a negative amount.")
            return None
        elif amount > account_0_balance:
            print("You can not withdrawl more than you have in your account.")
            return None
        account_0_balance -= amount
        return account_0_balance
    if account_number == 1:
        if password != account_1_password:
            print("Incorrect password")
            return None
        elif amount < 0:
            print("You can not withdrawl a negative amount.")
            return None
        elif amount > account_1_balance:
            print("You can not withdrawl more than you have in your account.")
            return None
        account_1_balance -= amount
        return account_1_balance


new_account(0, "Guilherme", 100, "secret")
new_account(1, "Luciana", 200, "secret")

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
        account_number = int(input("Enter your account number: "))
        user_password = input("Enter the password: ")
        the_balance = get_balance(account_number, user_password)
        if the_balance is not None:
            print(f"Your balance is: {the_balance}")
    elif action == "d":
        print("Deposit:")
        account_number = int(input("Enter your account number: "))
        user_password = input("Enter the password: ")
        amount = input("Enter the amount you want to deposit: ")
        amount = int(amount)
        new_balance = deposit(account_number, user_password, amount)
        if deposit is not None:
            print(f"Your balance is: {new_balance}")
    elif action == "w":
        print("Withdrawl:")
        account_number = int(input("Enter your account number: "))
        user_password = input("Enter the password: ")
        amount = input("Enter the amount you want to withdrawl: ")
        amount = int(amount)
        new_balance = withdrawl(account_number, user_password, amount)
        if withdrawl is not None:
            print(f"Your balance is: {new_balance}")
    elif action == "s":
        account_number = int(input("Enter your account number: "))
        user_password = input("Enter the password: ")
        show(account_number, user_password)
    elif action == "q":
        print("Bye")
        break
