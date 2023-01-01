import threading


class BankAccount:
    def __init__(self,account_num,holder_name):
        self.holder_name = holder_name
        self.account_num = account_num
        self.balance = 0
        self.transactions_list=[]
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            self.transactions_list.append(amount)

    def withdraw(self, amount):
        with self.lock:
            if self.balance>=amount:
                self.balance-=amount
                self.transactions_list.append(amount)
            else:
                return None


    def get_balance(self, amount):
        return self.balance


if __name__ == '__main__':
   my_account = BankAccount(123456, "Israel Israeli")

   def multiple_transactions_deposit(account):
       for i in range(100, 2000000, 10):
           account.deposit(i)

   def multiple_transactions_withdraw(account):
       for i in range(100, 2000000, 10):
           account.withdraw(i)

   t1 = threading.Thread(target=multiple_transactions_deposit, args=(my_account,))
   t2 = threading.Thread(target=multiple_transactions_deposit, args=(my_account,))
   t3 = threading.Thread(target=multiple_transactions_withdraw, args=(my_account,))
   t4 = threading.Thread(target=multiple_transactions_withdraw, args=(my_account,))

   t1.start()
   t2.start()
   t3.start()
   t4.start()

   t1.join()
   t2.join()
   t3.join()
   t4.join()

   assert my_account.balance == 0,\
       f"Expected balance: 0, received: {my_account.balance}"
   assert len(my_account.transactions_list) == 799960, \
       f"Expected transactions: 799960, received: len(my_account.transactions_list)"
   print(my_account.balance)