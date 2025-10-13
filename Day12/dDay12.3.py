# Defining a class called BankAccount
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner      # account owner's name
        self.balance = balance  # current balance

    def deposit(self, amount):
        # Add money to the balance
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        # Withdraw only if enough balance
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New Balance: {self.balance}")


# Creating a BankAccount object
account = BankAccount("Temesgen", 500)

# Performing deposit and withdraw
account.deposit(200)    # balance = 700
account.withdraw(100)   # balance = 600
account.withdraw(1000)  # not enough money
