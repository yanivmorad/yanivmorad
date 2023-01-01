# from datetime import datetime
#
#
#
#     def get_balance(self):
#          return self.__ba
#  with open("C:\Users\yc\Downloads\alice_in_wonderland.txt") as alice:
# class EBook:
#     def __init__(self,book_path, num_page):
#         with open(f'{book_path}',"r") as fh:
#             book = fh.read()
#         words_book= book.split()
# #         while True:
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         return self.name
#
# class Student(Person):
#     def __init__(self,grads):
#         super().__init__(name)
#         self.grads = grads
#     def __str__(self):
#         return f"{super(self.name)} {self.grads}"
# print(Student("yaniv",90))
# class BankAccount:
#     def __init__(self, holder_name, holder_id, holder_address, bank_name, bank_branch, maximum_credit):
#         self.holder_name = holder_name
#         self.holder_id = holder_id
#         self.holder_address = holder_address
#         self.bank_name = bank_name
#         self.bank_branch = bank_branch
#         self.maximum_credit = maximum_credit
#         self.balance_shekel = 0
#         self.balance_usd = 0
#         self.details = {}
#
# class Transaction(BankAccount):
#
#     def __init__(self, transaction_type: str, amount: float, currency: str):
#         super().__init__( holder_name, holder_id, holder_address, bank_name, bank_branch, maximum_credit):
#         self.transaction_type = transaction_type
#         self.amount = amount
#         self.currency = currency
#
#
#
#
#     def deposit_shekel(self, dte, deposit_amount):
#         if deposit_amount < 0:
#             return False
#         self.balance_shekel += deposit_amount
#         self.details[dte] = f"deposit shekel {deposit_amount}"
#
#     def deposit_dollar(self, date, deposit_amount):
#         if deposit_amount < 0:
#             return False
#         self.balance_usd += deposit_amount
#         self.details[date] = f"deposit_dollar{deposit_amount}"
#
#     def withdrawal(self, date, withdrawal_amount):
#         if self.balance_shekel + self.maximum_credit < withdrawal_amount:
#             return False
#
#         self.balance_shekel -= withdrawal_amount
#         self.details[date] = f"withdrawal{withdrawal_amount}"
#
#     def conversion_to_USD(self, date, conversion_amount: int):
#         if self.balance_shekel < conversion_amount:
#             return False
#         self.balance_usd += (conversion_amount / 3.4)
#         self.balance_shekel -= conversion_amount
#         self.details[date] = f"conversion_to_USD{conversion_amount}"
# from datetime import datetime
#
#
# class Person:
#
#     def __init__(self, person_id: str, name: str, address: str, phone: str):
#         self.id = person_id
#         self.name = name
#         self.address = address
#         self.phone = phone
#
#
# class Transaction:
#
#     def __init__(self,date, amount: float, currency: str):
#         self.date = datetime.date(date)
#         self.amount = amount
#         self.currency = currency
#
#     def __repr__(self):
#          return f"{datetime.date(self.date)} "
#
#
# class BankAccount:
#
#     def __init__(self, bank_name: str, branch: str, account_num: int, holders: set[Person],
#                  usd_allowed: bool = False, credit_limit: float=0):
#         self.bank_name: str = bank_name
#         self.branch: str = branch
#         self.account_num: int = account_num
#         self.holders: set[Person] = holders
#
#         self.nis_balance: float = 0
#         self.usd_balance: float = 0
#         self.usd_allowed: bool = usd_allowed
#         self.nis_credit_limit: float = credit_limit
#
#         self.transactions: dict[datetime.date: list[Transaction]] = {}
#
#     def __str__(self):
#         return f"Account {self.account_num}"
#
#     @staticmethod
#     def _valid_params(amnt, currency):
#         return amnt > 0 and currency in ('nis', 'usd')
#
#     def _add_transaction(self, transaction_type: str, amount: float, currency: str):
#         transaction_date = datetime.today()
#
#         # add new dictionary key if needed
#         if transaction_date not in self.transactions:
#             self.transactions[transaction_date] = []
#
#         # if we are here, we are sure that the key already exists
#         self.transactions[transaction_date].append(
#             Transaction(transaction_type, amount, currency)
#         )
#
#     def withdraw(self, amount: float, currency: str = 'nis') -> bool:
#
#         if not self._valid_params(amount, currency):
#             return False
#
#         if currency == 'nis':
#             if self.nis_balance - amount >= (self.nis_credit_limit * -1):
#                 self.nis_balance -= amount
#             else:
#                 return False
#         else:
#             if self.usd_allowed and self.usd_balance >= amount:
#                 self.usd_balance -= amount
#             else:
#                 return False
#         self._add_transaction('withdraw', amount=amount, currency=currency)
#         return True
#
#     def deposit(self, amount: float, currency: str = 'nis'):
#         if not self._valid_params(amount, currency):
#             return False
#
#         if currency == 'nis':
#             self.nis_balance += amount
#             self._add_transaction('deposit', amount=amount, currency=currency)
#             return True
#         else:
#             if not self.usd_allowed:
#                 return False
#             else:
#                 self._add_transaction('deposit', amount=amount, currency=currency)
#                 self.usd_balance += amount
#
#     def convert_to_usd(self, nis_amnt, nis2usd_exchange_rate):
#         if nis_amnt < 0:
#             return False
#         if not self.usd_allowed or self.nis_balance - nis_amnt < (self.nis_credit_limit * -1):
#             return False
#         self.nis_balance -= nis_amnt
#         self.usd_balance += nis_amnt * nis2usd_exchange_rate
#         self._add_transaction('convert_to_usd', amount=nis_amnt, currency='nis')
#         return True
#
#     def convert_to_nis(self, usd_amnt, usd2nis_exchange_rate):
#         if usd_amnt < 0:
#             return False
#         if not self.usd_allowed or self.usd_balance < usd_amnt:
#             return False
#         self.nis_balance += usd_amnt * usd2nis_exchange_rate
#         self.usd_balance -= usd_amnt
#         self._add_transaction('convert_to_nis', amount=usd_amnt, currency='usd')
#         return True
#
#     def get_current_balance(self) -> tuple[float, float]:
#         return self.nis_balance, self.usd_balance
#
#     def get_transactions_per_date(self, date: datetime.date) -> list[Transaction]:
#         return self.transactions.get(date, [])
#
#
# class Deposit(Transaction):
#     def __init__(self,date, amount: float, currency: str):
#         super().__init__(date,amount,currency)
#     def __str__(self):
#        super().__str__(Transaction)
#
#     def __repr__(self):
#         return f"deposit - {self.amount}{self.currency}"
#
# class Withdrawal(Transaction):
#     def __init__(self,date, amount: float, currency: str):
#         super().__init__(date,amount,currency)
#     def __str__(self):
#        super().__str__(Transaction)
#     def __repr__(self):
#       return f"withdrawal - {self.amount}{self.currency}"
#
# import abc
# import csv
# import json
# import os
#
#
# class TextFile(abc.ABC):
#     def __init__(self, file_path):
#         self.file_path = file_path
#         self.file_exists = os.path.exists(self.file_path)
#         if not self.file_exists:
#             raise FileNotFoundError('File does not exist')
#
#     def get_file_size(self):
#         return os.stat(self.file_path).st_size
#
#     @abc.abstractmethod
#     def get_content(self):
#         pass
#
# class CsvFile(TextFile):
#     def __init__(self, file_path, delimiter=','):
#         super().__init__(file_path)
#         self.delimiter = delimiter
#
#     def get_content(self):
#         with open(self.file_path) as file:
#             reader = csv.DictReader(file, delimiter=self.delimiter)
#             return [row for row in reader]
#
#     def get_rows_num(self):
#         with open(self.file_path) as file:
#             reader = csv.reader(file, delimiter=self.delimiter)
#             return sum(1 for row in reader)
#
#     def get_columns_num(self):
#         with open(self.file_path) as file:
#             reader = csv.reader(file, delimiter=self.delimiter)
#             return len(next(reader))
#
#     def get_row(self, row_num):
#         with open(self.file_path) as file:
#             reader = csv.DictReader(file, delimiter=self.delimiter)
#             for i, row in enumerate(reader):
#                 if i == row_num:
#                     return row
#             return {}
#
#     def get_column(self, column_num):
#         with open(self.file_path) as file:
#             reader = csv.reader(file, delimiter=self.delimiter)
#             return [row[column_num] for row in reader]
#
#     def get_cell(self, row_num, column_num):
#         with open(self.file_path) as file:
#             reader = csv.reader(file, delimiter=self.delimiter)
#             for i, row in enumerate(reader):
#                 if i == row_num:
#                     return row[column_num]
#             return ''
#
# class JsonFile(TextFile):
#     def get_content(self):
#         with open(self.file_path) as file:
#             return json.load(file)
#
#     def is_list(self):
#         with open(self.file_path) as file:
#             return isinstance(json.load(file), list)
#
import json
import os

#     def is_object(self):
#         with open(self.file_path) as file:
#             return isinstance(json.load(file), dict)
# def judgeCircle( moves):
#     """
#     :type moves: str
#     :rtype: bool
#     """
#     l_moves = list(moves)
#     u = []
#     d = []
#     l = []
#     r = []
#     for i in l_moves:
#         if i == "U":
#             u.append(i)
#         if i == "R":
#             r.append(i)
#         if i == "L":
#             l.append(i)
#         if i == "D":
#             d.append(i)
#     if len(u) == len(d) and len(r) == len(l):
#         return True
#     else:
#         return False
#
# print(judgeCircle("LL"))
# d ={2:12,1:32}
#
# input("dfd, fvvf fvv".split(","))
# os.system('cls')
# print("Fgd")
# with open("files/sample4.json", 'r') as jfile:
#     # data = json.load(jfile)
#     for data in json.load(jfile).values():
#         print(data)
dir1, name1 = os.path.split("files/sample4.json")
print(name1)