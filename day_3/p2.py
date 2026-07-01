#encapsulation
class Bank:
    def __init__(self) :
        self .__balance = 5000

    def deposit(self, amount):
        self .__balance += amount

    def show_balance(self):
        print(self.__balance)

b = Bank()
b.deposit(6000)
b.show_balance()