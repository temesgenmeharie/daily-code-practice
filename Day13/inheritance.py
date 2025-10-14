# Parent class (Base class)
class Animal:
    def speak(self):
        # Generic behavior
        print("This animal makes a sound.")

# Child class (inherits from Animal)
class Dog(Animal):
    def speak(self):
        # Overriding the parent method with specific behavior
        print("The dog barks: Woof Woof!")

# Creating objects
animal = Animal()
dog = Dog()

# Calling speak() from both classes
animal.speak()  # from Animal
dog.speak()     # from Dog (overridden)
