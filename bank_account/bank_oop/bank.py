from account import AbortTransaction, Account


class Bank:
    def __init__(self, hours, address, phone):
        self.account_dict = {}
        self.next_account_number = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def ask_for_valid_account_number(self):
        account_number = input('What is your account number? ')
        try:
            account_number = int(account_number)
        except ValueError:
            raise AbortTransaction('The account number must be an integer')
        if account_number not in self.account_dict:
            raise AbortTransaction(f'There is no account {account_number}')
        return account_number

    def ask_for_valid_password(self, account):
        password = input('Please enter your password: ')
        account.check_password_match(password)

    def get_user_account(self):
        account_number = self.ask_for_valid_account_number()
        the_account = self.account_dict[account_number]
        self.ask_for_valid_password(the_account)
        return the_account

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
        the_account = self.get_user_account()
        the_balance = the_account.get_balance()
        print(f'You had {the_balance} in your account, which is being returned to you.')
        del the_account
        print('Your account is closed.')

    def balance(self):
        print('*** Get Balance ***')
        the_account = self.get_user_account()
        the_balance = the_account.get_balance()
        print(f'Your balance is: {the_balance}')

    def deposit(self):
        print('*** Deposit ***')
        the_account = self.get_user_account()
        deposit_amount = input('Please enter the amount to deposit: ')
        the_balance = the_account.deposit(deposit_amount)
        print(f'Deposited: {deposit_amount}')
        print(f'Your new balance is: {the_balance}')

    def withdraw(self):
        print('*** Withdraw ***')
        the_account = self.get_user_account()
        withdraw_amount = int(input('Please enter the amount to withdraw: '))
        the_balance = the_account.withdraw(withdraw_amount)
        print(f'Withdraw: {withdraw_amount}')
        print(f'Your new balance is: {the_balance}')

    def get_info(self):
        print(f'Hours: {self.hours}')
        print(f'Address: {self.address}')
        print(f'Phone: {self.phone}')
        print(f'We currently have {len(self.account_dict)} account(s) open.')

    def show(self):
        the_account = self.get_user_account()
        the_account.show()


