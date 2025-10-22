# ----------------------------------------
# Employee Management System (Day 18)
# Demonstrates OOP concepts: Class, Object,
# Encapsulation, Inheritance, and Polymorphism
# ----------------------------------------

# 1️⃣ Parent Class
class Employee:
    def __init__(self, name, emp_id, salary):
        # Attributes (Encapsulation)
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    # Method to display employee details
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary}")

    # Method to calculate yearly salary
    def yearly_salary(self):
        return self.salary * 12


# 2️⃣ Child Class (Inheritance)
class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        # Inherit from Employee class using super()
        super().__init__(name, emp_id, salary)
        self.department = department

    # Override method (Polymorphism)
    def display_info(self):
        print(f"[Manager Info]")
        super().display_info()
        print(f"Department: {self.department}")


# 3️⃣ Another Child Class (Inheritance)
class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language

    # Override method (Polymorphism)
    def display_info(self):
        print(f"[Developer Info]")
        super().display_info()
        print(f"Programming Language: {self.programming_language}")


# 4️⃣ Demonstration (Creating Objects)
if __name__ == "__main__":
    # Create Manager Object
    manager1 = Manager("Alice", "M101", 9000, "IT")
    # Create Developer Object
    dev1 = Developer("Bob", "D202", 7000, "Python")

    # Display info for both
    print("=== Employee Details ===")
    manager1.display_info()
    print()
    dev1.display_info()

    # Calculate and show yearly salary
    print("\n=== Yearly Salaries ===")
    print(f"{manager1.name}: ${manager1.yearly_salary()}")
    print(f"{dev1.name}: ${dev1.yearly_salary()}")
