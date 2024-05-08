class Balance:
    def __init__(self, taka):
        self.__balance =taka   # Private attribute
        self.increment=0       # Public Atribute

    def increase(self, amount):
        self.__balance += amount
        self.increment+=amount

    def current_balance(self):
        return self.__balance

balance = Balance(50)
balance.increase(20)
print(balance.current_balance())  # Output: 70
print(balance.increment)           # Output: 20
print(balance.__balance)  # Error: 'balance' object has no attribute '__balance'

