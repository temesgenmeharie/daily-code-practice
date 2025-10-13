# Class representing a phone
class Phone:
    def __init__(self, brand, price):
        self.brand = brand   # phone brand
        self.price = price   # phone price

    def call(self):
        # method to show making a call
        print(f"Calling using {self.brand} phone.")

# Creating objects
p1 = Phone("Samsung", 500)
p2 = Phone("iPhone", 1200)

# Using method
p1.call()
p2.call()
print(f"Phone 1: {p1.brand}, Price: {p1.price}")
print(f"Phone 2: {p2.brand}, Price: {p2.price}")