from .bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, withdrawal_limit=20000):
        super().__init__(owner, balance)
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            return f"Limit exceeded: Max allowed is ₦{self.withdrawal_limit}"
        return super().withdraw(amount)
