from bank import Bank


the_bank = Bank()

while True:
    print()
    print('Press b to get the balance')
    print('Press c to close an account')
    print('Press d to make a deposit')
    print('Press o to open a new account')
    print('Press w to make a withdraw')
    print('Press s to show your account data')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ').lower()
    action = action[0]
    print()

    if action == 'b':
        the_bank.balance()
    elif action == 'c':
        the_bank.close_account()
    elif action == 'd':
        the_bank.deposit()
    elif action == 'o':
        the_bank.open_account()
    elif action == 's':
        the_bank.show()
    elif action == 'w':
        the_bank.withdraw()
    elif action == 'q':
        break
    else:
        print('Sorry, that was not a valid action. Please try again.')
print('Done')
