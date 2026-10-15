from accounts import Account, SavingsAccount, CheckingAccount
from exceptions import DuplicateAccountError, AccountNotFoundError, InvalidTransferError

class Bank:
    """A bank that keeps track of all accounts by account number."""
    def __init__(self, name):
        self.name = name
        self._accounts = {}

    def create_account(self, account_number, holder_name, balance=0, account_type="basic"):
        """Open a new account and store it by account number."""
        if account_number in self._accounts:
            raise DuplicateAccountError("Account number already exists.")

        if account_type == "savings":
            account = SavingsAccount(account_number, holder_name, balance)

        elif account_type == "checking":
            account = CheckingAccount(account_number, holder_name, balance)

        else:
            account = Account(account_number, holder_name, balance)

        self._accounts[account_number] = account
        return account

    def get_account(self, account_number):
        """Find an account by its account number."""
        if account_number not in self._accounts:
            raise AccountNotFoundError("Account not found.")
        return self._accounts[account_number]

    def transfer(self, from_number, to_number, amount):
        """Move money from one account to another."""
        if from_number == to_number:
            raise InvalidTransferError("Cannot transfer to the same account.")

        source = self.get_account(from_number)
        destination = self.get_account(to_number)
        source.withdraw(amount)
        destination.deposit(amount)

    