from select import select
import unittest

from account import Account


class AccountTest(unittest.TestCase):
    def setUp(self):
        self.account = Account('test', 100, password='secret')
    
    def test_deposit_incorrect_password(self):
        """
        deposit won't be made if password is incorrect.
        """
        self.account.deposit(100, 'wrong')
        self.assertEqual(self.account.balance, 100)

    def test_deposit_negative_amount(self):
        """
        Cannot deposit a negative amount.
        """
        self.account.deposit(-100, 'secret')
        self.assertEqual(self.account.balance, 100)

    def test_deposit(self):
        """
        must add amount to the account balance.
        """
        self.account.deposit(100, 'secret')
        self.assertEqual(self.account.balance, 200)
    
    def test_withdraw_incorrect_password(self):
        """
        withdraw won't be made if password is incorrect.
        """
        self.account.withdraw(100, 'wrong')
        self.assertEqual(self.account.balance, 100)

    def test_withdraw_negative_amount(self):
        """
        Cannot withdraw a negative amount.
        """
        self.account.withdraw(-100, 'secret')
        self.assertEqual(self.account.balance, 100)

    def test_withdraw(self):
        """
        must subtract amount to the account balance.
        """
        self.account.withdraw(100, 'secret')
        self.assertEqual(self.account.balance, 0)
    
    def test_get_balance_incorrect_password(self):
        """
        Must not show balance if password is wrong.
        """
        self.assertEqual(self.account.get_balance('worng'), None)

    def test_get_balance(self):
        """
        Must show balance value.
        """
        self.assertEqual(self.account.get_balance('secret'), 100)


if __name__=='__main__':
    unittest.main()