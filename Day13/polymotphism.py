class Cat:
    def speak(self):
        print("The cat meows: Meow!")

class Dog:
    def speak(self):
        print("The dog barks: Woof!")

# Function that accepts any object with speak()
def animal_sound(animal):
    animal.speak()

# Creating objects
cat = Cat()
dog = Dog()

# Calling the same function with different objects
animal_sound(cat)  # Cat's speak()
animal_sound(dog)  # Dog's speak()
