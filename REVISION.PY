class Account:
    def __init__(self, balance=5000):
        self._balance = balance

    def withdraw(self, amount):
        print("Withdraw not defined")

    def show_balance(self):
        print("Balance: ", self._balance)

class Savings(Account):
    def withdraw(self, amount):
        if self._balance - amount >= 500:
            self._balance -= amount
            print("Amount left: ", self._balance)
        else:
            print("Min balance required")


a = Account()
s= Savings()

# a.withdraw(400)
s.withdraw(400)
