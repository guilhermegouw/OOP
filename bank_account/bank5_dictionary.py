accounts_list = []

def new_account(name, balance, password):
    global accounts_list
    account_dict = {"a_name": name, "a_balance": balance, "a_password": password}
    accounts_list.append(account_dict)


def show(account_number, password):
    global accounts_list
    account = accounts_list[account_number]
    if password != account["a_password"]:
        print("Incorrect password")
        return None
    print()
    print(f"Account: {account_number}")
    print(f"Name: {account['a_name']}")
    print(f"Balance: {account['a_balance']}")
    print(f"Password: {account['a_password']}")
    print()


def get_balance(account_number, password):
    global accounts_list
    account = accounts_list[account_number]
    if password != account["a_password"]:
        print("Incorrect password")
        return None
    return account['a_balance']


def deposit(account_number, password, amount):
    global accounts_list
    account = accounts_list[account_number]
    if password != account["a_password"]:
        print("Incorrect password")
        return None
    elif amount < 0:
        print("You can not deposit a negative amount.")
        return None
    account['a_balance'] += amount
    return account['a_balance']


def withdrawl(account_number, password, amount):
    global accounts_list
    account = accounts_list[account_number]
    if password != account["a_password"]:
        print("Incorrect password")
        return None
    elif amount < 0:
        print("You can not withdrawl a negative amount.")
        return None
    elif amount > account['a_balance']:
        print("You can not withdrawl more than you have in your account.")
        return None
    account['a_balance'] -= amount
    return account['a_balance']


print(f"Guilherme's account number: {len(accounts_list)}")
new_account("Guilherme", 100, "secret")
print(f"Luciana's account number: {len(accounts_list)}")
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
