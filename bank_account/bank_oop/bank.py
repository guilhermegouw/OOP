from account import Account


class Bank:
    def __init__(self):
        self.account_dict = {}
        self.next_account_number = 0

    def create_account(self, name, starting_amount, password):
        the_account = Account(name, starting_amount, password)
        new_account_number = self.next_account_number
        self.account_dict[new_account_number] = the_account
        self.next_account_number += 1
        return new_account_number
    
    def open_account(self):
        print('*** Open Account ***')
        username = input('What is the name for the new user account? ')
        user_starting_amount = int(input('What is the starting balance for this account? '))
        user_password = input('What is the password you want to use for this account? ')
        user_account_number = self.create_account(username, user_starting_amount, user_password)
        print('Your new account number is: ', user_account_number)
        print()
    
    def close_account(self):
        print('*** Close Account ***')
        user_account_number = int(input('What is your account number? '))
        user_password = input('What is your password? ')
        the_account = self.account_dict[user_account_number]
        the_balance = the_account.get_balance(user_password)
        if the_balance is not None:
            print(f'You had {the_balance} in your account, which is being returned to you.')
            del self.account_dict[user_account_number]
            print('Your account is closed.')

    def balance(self):
        print('*** Get Balance ***')
        user_account_number = int(input('What is your account number? '))
        user_password = input('What is your password? ')
        the_account = self.account_dict[user_account_number]
        the_balance = the_account.get_balance(user_password)
        if the_balance is not None:
            print(f'Your balance is: {the_balance}')

    def deposit(self):
        print('*** Deposit ***')
        user_account_number = int(input('What is your account number? '))
        deposit_amount = int(input('Please enter the amount to deposit: '))
        user_password = input('What is your password? ')
        the_account = self.account_dict[user_account_number]
        the_balance = the_account.deposit(deposit_amount, user_password)
        if the_balance is not None:
            print(f'Your new balance is: {the_balance}')

    def withdraw(self):
        print('*** Withdraw ***')
        user_account_number = int(input('What is your account number? '))
        withdraw_amount = int(input('Please enter the amount to withdraw: '))
        user_password = input('What is your password? ')
        the_account = self.account_dict[user_account_number]
        the_balance = the_account.withdraw(withdraw_amount, user_password)
        if the_balance is not None:
            print(f'Withdraw: {withdraw_amount}')
            print(f'Your new balance is: {the_balance}')

    def show(self):
        user_account_number = int(input('What is your account number? '))
        user_password = input('What is your password? ')
        the_account = self.account_dict[user_account_number]
        the_account.show(user_password)


