# 5. Create a bank account class that has attributes `owner`, `balance` and two methods `deposit` and `withdraw`. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
#class Account:
#    pass

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

acc = Account("John Doe", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(150) 

