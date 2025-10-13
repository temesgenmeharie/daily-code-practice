# Defining a class called Student
class Student:
    def __init__(self, name, grade):
        self.name = name    # attribute 1
        self.grade = grade  # attribute 2

    def show_details(self):
        # method to display student info
        print(f"Student Name: {self.name}, Grade: {self.grade}")


# Creating objects (instances of Student class)
s1 = Student("John", "A")
s2 = Student("Alice", "B+")

# Calling the method for each object
s1.show_details()
s2.show_details()
        