# Defining a class called Car
class Car:
    def __init__(self, brand, color):
        self.brand = brand   # brand of the car
        self.color = color   # color of the car

    def drive(self):
        # method that represents driving the car
        print(f"The {self.color} {self.brand} is driving.")


# Creating car objects
car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Black")

# Calling drive() method
car1.drive()
car2.drive()
