class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount
        print ('Your current balance :', self.__balance)
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f'Your current balance: {self.__balance}')
        else:
            print("Not enough balance!")

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
depo = int(input('Enter deposit amount: '))
acc.deposit(depo)
draw = int(input('Enter withdraw amount: '))
acc.withdraw(draw)
print("💰 Balance:", acc.get_balance())
