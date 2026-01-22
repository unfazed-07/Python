from datetime import datetime
class Account:
    def __init__(self, balance=5000):
        self._balance = balance
        self.history = []


    def withdraw(self, amount):
        print("Withdraw not defined")

    def show_balance(self):
        print("Balance: ", self._balance)

    def show_history(self):
        if not self.history:
            print("No transaction history till now!")
            return

        for entry in self.history:
            print(entry)

    def set_password(self, password):
        self.password=password

class Savings(Account):
    def withdraw(self, amount):
        enter = input("Enter the password: ")
        if enter != self.password:
            print("Invali password! Try again")
            return 
        if self._balance - amount >= 500:
            self._balance -= amount
            print("Amount withdrawn: ", amount,", Total Balance: ", self._balance, datetime.now().strftime("on date: %d-%m-%Y at time: %H:%M:%S"))
            log = f"Amount withdrawn: {amount}  Total Balance:  {self._balance} {datetime.now().strftime("on date: %d-%m-%Y at time: %H:%M:%S")}"
            self.history.append(log)
        else:
            print("Min balance required")

    def deposit(self, amount):
        self._balance += amount
        print("Amount depostied: ", amount, ", Total Balance: ", self._balance, datetime.now().strftime("on date: %d-%m-%Y at time: %H:%M:%S"))
        log = f"Amount deposited: {amount}  Total Balance:  {self._balance} {datetime.now().strftime("on date: %d-%m-%Y at time: %H:%M:%S")}"
        self.history.append(log)

a = Account()
s= Savings()

s.show_history()