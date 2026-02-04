class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостатньо коштів або неправильна сума!")

    def get_balance(self):
        return self.__balance

acc = BankAccount(200)
acc.deposit(100)
acc.withdraw(50)
print(acc.get_balance())

acc.__balance = 1000
print(acc.get_balance())
