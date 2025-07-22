"""
Kata: BankAccount Class

Goal:
    Practice working with internal state
    Implement deposit and withdrawal logic
    Protect balance from going negative

Required Behaviors:
    - deposit(amount) adds to balance
    - withdraw(amount) subtracts from balance
    - get_balance() returns current balance

Constraints:
    - No negative deposits or withdrawals
    - Withdrawing more than balance should raise an error
    - Use TDD (failing test → pass → refactor)
    - No external libraries
"""

import pytest

from leve_1.code.bank_account import BankAccount


def test_bank_account_initialization():
    account = BankAccount()
    assert isinstance(account, BankAccount)
    assert account.get_balance() == 0


def test_bank_account_positive_deposit():
    account = BankAccount()
    account.deposit(100)
    assert account.get_balance() == 100


def test_bank_account_negative_deposit():
    account = BankAccount()
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        account.deposit(-50)


def test_bank_account_withdrawal():
    account = BankAccount()
    account.deposit(200)
    account.withdraw(50)
    assert account.get_balance() == 150


def test_bank_account_withdrawal_exceeds_balance():
    account = BankAccount()
    account.deposit(100)
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(150)


def test_bank_account_negative_withdrawal():
    account = BankAccount()
    with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
        account.withdraw(-50)
