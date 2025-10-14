class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner         # public attribute
        self.__balance = balance   # private attribute (cannot be accessed directly)

    def deposit(self, amount):
        self.__balance += amount   # modify balance safely
        print(f"Deposited {amount}. New Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.__balance}")

    def get_balance(self):          # getter method
        return self.__balance


# Creating an object
acc = BankAccount("Temesgen", 500)

acc.deposit(200)
acc.withdraw(100)
print("Final Balance:", acc.get_balance())
