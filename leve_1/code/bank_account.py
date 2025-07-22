class BankAccount:
    def __init__(self):
        self._balance = 0

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._validate_positive_amount(amount, "Deposit")
        self._balance += amount

    def withdraw(self, amount):
        self._validate_positive_amount(amount, "Withdrawal")
        if self._balance < amount:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def _validate_positive_amount(self, amount, caller):
        if amount <= 0:
            raise ValueError(f"{caller} amount must be positive")
        return True
