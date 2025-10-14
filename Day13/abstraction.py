from abc import ABC, abstractmethod

# Abstract class (cannot be instantiated)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # abstract method, must be implemented in child classes


# Rectangle class implementing area()
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Circle class implementing area()
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# Creating objects
rect = Rectangle(5, 4)
circle = Circle(3)

print("Rectangle Area:", rect.area())
print("Circle Area:", circle.area())
