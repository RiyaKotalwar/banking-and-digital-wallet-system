class BankingError(Exception):
    """Base class for all banking-related errors."""


class InvalidAmountError(BankingError):
    """Raised when an amount is zero or negative."""


class InsufficientFundsError(BankingError):
    """Raised when there aren't enough funds in an account."""


class AccountNotFoundError(BankingError):
    """No such account is created."""


class DuplicateAccountError(BankingError):
    """Raised when an account number already exists in the bank."""


class InvalidTransferError(BankingError):
    """Raised when a transfer is not allowed, such as to the same account."""

    