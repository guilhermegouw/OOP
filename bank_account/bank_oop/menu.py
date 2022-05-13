from account import AbortTransaction
from bank import Bank


the_bank = Bank('9 to 5', '123 Main Street, AnyTown, USA', '(650) 555-1212')

while True:
    print()
    print('Press b to get the balance')
    print('Press c to close an account')
    print('Press d to make a deposit')
    print('Press i to get Bank information')
    print('Press o to open a new account')
    print('Press w to make a withdraw')
    print('Press s to show your account data')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ').lower()
    action = action[0]
    print()

    try:
        if action == 'b':
            the_bank.balance()
        elif action == 'c':
            the_bank.close_account()
        elif action == 'd':
            the_bank.deposit()
        elif action == 'i':
            the_bank.get_info()
        elif action == 'o':
            the_bank.open_account()
        elif action == 's':
            the_bank.show()
        elif action == 'w':
            the_bank.withdraw()
        elif action == 'q':
            break
    except AbortTransaction as error:
        print(error)
print('Done')
