import random


class BankAccount:
    def __init__(self, holder_name, holder_id, holder_address, bank_name, bank_branch, maximum_credit, usd: bool):
        self.holder_name = holder_name
        self.holder_id = holder_id
        self.holder_address = holder_address
        self.bank_name = bank_name
        self.bank_branch = bank_branch
        self.account_number = random.randint(10000, 99999)
        self.maximum_credit = maximum_credit
        self.usd = usd
        self.balance_shekel = 0
        self.balance_usd = None
        self.details = {}
        if self.usd:
            self.balance_usd = 0

    def deposit_shekel(self, dte, deposit_amount):
        if deposit_amount < 0:
            return False
        self.balance_shekel += deposit_amount
        self.details[dte] = f"deposit shekel {deposit_amount}"

    def deposit_dollar(self, date, deposit_amount):
        if deposit_amount < 0:
            return False
        self.balance_usd += deposit_amount
        self.details[date] = f"deposit_dollar{deposit_amount}"

    def withdrawal(self, date, withdrawal_amount):
        if self.balance_shekel + self.maximum_credit < withdrawal_amount:
            return False

        self.balance_shekel -= withdrawal_amount
        self.details[date] = f"withdrawal{withdrawal_amount}"

    def conversion_to_USD(self, date, conversion_amount: int):
        if self.balance_shekel < conversion_amount:
            return False
        self.balance_usd += (conversion_amount / 3.4)
        self.balance_shekel -= conversion_amount
        self.details[date] = f"conversion_to_USD{conversion_amount}"


user_1 = BankAccount("yaniv", 313313, "netanya", "hapolim", 21, 8000, True)
user_1.deposit_shekel("25.10", 1000)
user_1.deposit_shekel("4.1", 20000)
user_1.withdrawal("11.1", 3000)
user_1.conversion_to_USD("23.11", 10000)
print(user_1.balance_shekel, user_1.balance_usd, user_1.details)
print(user_1.details)
