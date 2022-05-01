account_name_list = []
account_balance_list = []
account_passwords_list = []


def new_account(name, balance, password):
    global account_name_list, account_balance_list, account_passwords_list
    account_name_list.append(name)
    account_balance_list.append(balance)
    account_passwords_list.append(password)


def show(account_number, password):
    global account_name_list, account_balance_list, account_passwords_list
    if password != account_passwords_list[account_number]:
        print("Incorrect password")
        return None
    print()
    print(f"Account: {account_number}")
    print(f"Name: {account_name_list[account_number]}")
    print(f"Balance: {account_balance_list[account_number]}")
    print(f"Password: {account_passwords_list[account_number]}")
    print()


def get_balance(account_number, password):
    global account_name_list, account_balance_list, account_passwords_list
    if password != account_passwords_list[account_number]:
        print("Incorrect password")
        return None
    return account_balance_list[account_number]


def deposit(account_number, password, amount):
    global account_name_list, account_balance_list, account_passwords_list
    if password != account_passwords_list[account_number]:
        print("Incorrect password")
        return None
    elif amount < 0:
        print("You can not deposit a negative amount.")
        return None
    account_balance_list[account_number] += amount
    return account_balance_list[account_number]


def withdrawl(account_number, password, amount):
    global account_name_list, account_balance_list, account_passwords_list
    if password != account_passwords_list[account_number]:
        print("Incorrect password")
        return None
    elif amount < 0:
        print("You can not withdrawl a negative amount.")
        return None
    elif amount > account_balance_list[account_number]:
        print("You can not withdrawl more than you have in your account.")
        return None
    account_balance_list[account_number] -= amount
    return account_balance_list[account_number]


new_account("Guilherme", 100, "secret")
new_account("Luciana", 200, "secret")

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
