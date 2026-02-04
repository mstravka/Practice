class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
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

acc = BankAccount("Іван", 100)
acc.deposit(50)
acc.withdraw(30)
print("Баланс:", acc.get_balance())

acc.__balance = 1000
print("Баланс після спроби прямого доступу:", acc.get_balance())
