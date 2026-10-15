from datetime import datetime


class Transaction: 
    """One record of a deposit, withdrawal, or transfer."""

    def __init__(self, transaction_type, amount, balance_after):
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance_after = balance_after
        self.timestamp = datetime.now()

    def __str__(self):
        time = self.timestamp.strftime("%Y-%m-%d %H:%M")
        return f"{time} | {self.transaction_type} | {self.amount:.2f} | Balance: {self.balance_after:.2f}"
        
        """"self._timestamp = datetime.now()
        
    @property
    def transaction_type(self):
        return self._transaction_type

    @property
    def amount(self):
        return self._amount

    @property
    def timestamp(self):
        return self._timestamp

    def __str__(self):
        return f"{self._transaction_type} | {self._amount} | {self._timestamp.strftime}"""""