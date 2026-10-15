from exceptions import InvalidAmountError, InsufficientFundsError
from transaction import Transaction

class Account:
    """A bank account with a holder, a balance and a transaction history."""
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self._balance = balance
        self._transactions = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        """Add money to the account and record the transaction."""        
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be greater than zero")
        self._balance += amount
        record = Transaction("deposit", amount, self._balance)
        self._transactions.append(record)

    def withdraw(self, amount):
        """Take money out of the account and record the transaction."""
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be greater than zero.")

        if amount > self._balance:
            raise InsufficientFundsError("Insufficient funds for this withdrawal.")

        self._balance -= amount
        record = Transaction("withdrawal", amount, self._balance)
        self._transactions.append(record)


    def get_statement(self):
        """Return one text line for each transaction."""
        lines = []
        for record in self._transactions:
            lines.append(str(record))
        return lines


class SavingsAccount(Account):
    """An account that earns interest on its balance."""
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.04):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate


    def add_interest(self):
        """Add interest to the balance and record the transaction."""
        interest = round(self._balance * self.interest_rate,2)
        self._balance += interest
        record = Transaction("interest", interest, self._balance)
        self._transactions.append(record)
        return interest


class CheckingAccount(Account):
    """An account that allows withdrawals beyond the balance up to an overdraft limit."""
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=1000):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Take money out, allowing the balance to go down to minus the overdraft limit."""

        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be greater than zero.")

        if amount > self._balance + self.overdraft_limit:
            raise InsufficientFundsError("Withdrawal exceeds balance and overdraft limit.")

        self._balance -= amount
        record = Transaction("withdrawal", amount, self._balance)
        self._transactions.append(record)

    


