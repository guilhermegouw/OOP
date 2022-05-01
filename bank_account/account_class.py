class Account():
    def __init__(self, name, balance, password) -> None:
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amount_to_deposit, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        if amount_to_deposit < 0:
            print('You cannot deposit a negative amount')
            return None
        self.balance += amount_to_deposit
        return self.balance
    
    def withdraw(self, amount_to_withdraw, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        if amount_to_withdraw < 0:
            print('You cannot withdraw a negative amount')
            return None
        if amount_to_withdraw > self.balance:
            print('You cannot withdraw more than you have in your account')
            return None
        self.balance -= amount_to_withdraw
        return self.balance
    
    def get_balance(self, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        return self.balance

    def show(self, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        print(f'Name: {self.name}')
        print(f'Balance: {self.balance}')
        print(f'Password: {self.password}')
        print()


if __name__=='__main__':
    account = Account('Guilherme', 100, 'secret')

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
            the_balance = account.get_balance(user_password)
            if the_balance is not None:
                print(f"Your balance is: {the_balance}")
        elif action == "d":
            print("Deposit:")
            user_password = input("Enter the password: ")
            amount = input("Enter the amount you want to deposit: ")
            amount = int(amount)
            new_balance = account.deposit(amount, user_password)
            if new_balance is not None:
                print(f"Your balance is: {new_balance}")
        elif action == "w":
            print("Withdrawl:")
            user_password = input("Enter the password: ")
            amount = input("Enter the amount you want to withdrawl: ")
            amount = int(amount)
            new_balance = account.withdraw(amount, user_password)
            if new_balance is not None:
                print(f"Your balance is: {new_balance}")
        elif action == "s":
            user_password = input("Enter the password: ")
            account.show(user_password)
        elif action == "q":
            print("Bye")
            break
