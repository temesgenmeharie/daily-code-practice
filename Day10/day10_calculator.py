# ----------------------------------------------
# Day 10 - Advanced Scientific Calculator (Interactive)
# ----------------------------------------------
# Features:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division (with zero protection)
# 5. Power (a^b)
# 6. Square Root
# 7. Percentage
# 8. Sine (degrees)
# 9. Cosine (degrees)
# 10. Tangent (degrees)
# 11. Exit
# ----------------------------------------------

import math  # Import math module for scientific operations

# 1️⃣ ADDITION
def add(a, b):
    return a + b  # Return the sum of a and b

# 2️⃣ SUBTRACTION
def subtract(a, b):
    return a - b  # Return the difference of a and b

# 3️⃣ MULTIPLICATION
def multiply(a, b):
    return a * b  # Return the product of a and b

# 4️⃣ DIVISION
def divide(a, b):
    if b == 0:  # Check division by zero
        return "Error! Cannot divide by zero."
    else:
        return a / b  # Return division result

# 5️⃣ POWER FUNCTION
def power(a, b):
    return a ** b  # Return a raised to the power of b

# 6️⃣ SQUARE ROOT
def square_root(a):
    if a < 0:  # Square root of negative number is invalid
        return "Error! Cannot take square root of negative number."
    else:
        return math.sqrt(a)  # Return square root

# 7️⃣ PERCENTAGE
def percentage(a, b):
    return (a / b) * 100  # Return a as percentage of b

# 8️⃣ SINE FUNCTION (degrees)
def sine(deg):
    rad = math.radians(deg)  # Convert degrees to radians
    return math.sin(rad)  # Return sine

# 9️⃣ COSINE FUNCTION (degrees)
def cosine(deg):
    rad = math.radians(deg)  # Convert degrees to radians
    return math.cos(rad)  # Return cosine

# 🔟 TANGENT FUNCTION (degrees)
def tangent(deg):
    if deg % 180 == 90:  # Tan undefined at 90, 270, etc.
        return "Error! Tangent undefined at this angle."
    rad = math.radians(deg)  # Convert degrees to radians
    return math.tan(rad)  # Return tangent

# ----------------------------------------------
# MAIN PROGRAM LOOP
# ----------------------------------------------
while True:  # Infinite loop for menu until user exits
    print("\n===== SCIENTIFIC CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (a^b)")
    print("6. Square Root")
    print("7. Percentage (a% of b)")
    print("8. Sine (degrees)")
    print("9. Cosine (degrees)")
    print("10. Tangent (degrees)")
    print("11. Exit")

    choice = input("Select an operation (1-11): ")  # Get user choice

    # ------------------------------------------
    # EXIT CONDITION
    if choice == '11':
        print("Exiting calculator. Goodbye!")
        break  # Stop the loop and exit program

    # ------------------------------------------
    # ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION, POWER, PERCENTAGE
    if choice in ['1','2','3','4','5','7']:
        try:
            num1 = float(input("Enter first number: "))  # First number
            num2 = float(input("Enter second number: "))  # Second number
        except ValueError:  # Handle invalid input
            print("Error! Please enter a valid number.")
            continue  # Go back to menu

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
        elif choice == '7':
            print(f"{num1} is {percentage(num1, num2)}% of {num2}")

    # ------------------------------------------
    # SQUARE ROOT
    elif choice == '6':
        try:
            num = float(input("Enter number: "))
        except ValueError:
            print("Error! Please enter a valid number.")
            continue
        print("Result:", square_root(num))

    # ------------------------------------------
    # SINE, COSINE, TANGENT
    elif choice in ['8','9','10']:
        try:
            angle = float(input("Enter angle in degrees: "))
        except ValueError:
            print("Error! Please enter a valid number.")
            continue

        if choice == '8':
            print("sin(", angle, ") =", sine(angle))
        elif choice == '9':
            print("cos(", angle, ") =", cosine(angle))
        elif choice == '10':
            print("tan(", angle, ") =", tangent(angle))

    # ------------------------------------------
    # INVALID CHOICE
    else:
        print("Invalid choice! Please select a number between 1 and 11.")
