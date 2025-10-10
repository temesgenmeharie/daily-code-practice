# ----------------------------------------------
# Temperature Converter (Advanced Version)
# ----------------------------------------------
# This program converts temperatures between:
# Celsius, Fahrenheit, and Kelvin
# It uses:
# - Functions
# - Menu system (while loop)
# - Input validation (try/except)
# - Clear output with units
# - Infinite loop until user exits

# -----------------------------
# 1️⃣ Define Conversion Functions
# -----------------------------

def celsius_to_fahrenheit(c):
    # Formula: (C × 9/5) + 32
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    # Formula: (F - 32) × 5/9
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    # Formula: C + 273.15
    return c + 273.15

def kelvin_to_celsius(k):
    # Formula: K - 273.15
    return k - 273.15

def fahrenheit_to_kelvin(f):
    # Formula: (F - 32) × 5/9 + 273.15
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    # Formula: (K - 273.15) × 9/5 + 32
    return (k - 273.15) * 9/5 + 32


# --------------------------------------
# 2️⃣ MAIN PROGRAM (Menu + Loop + Logic)
# --------------------------------------
while True:
    # Show menu to the user
    print("\n=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    # Ask user to choose an option
    choice = input("Select an option (1-7): ")

    # If user chooses 7, exit the loop (end program)
    if choice == '7':
        print("Exiting... Goodbye!")
        break

    # If user enters a valid option (1-6)
    if choice in ['1', '2', '3', '4', '5', '6']:
        # Use try/except to validate the temperature input
        try:
            # Ask user to input a temperature value
            temp = float(input("Enter the temperature value: "))
        except ValueError:
            # If user enters something invalid (e.g. 'abc')
            print("Invalid input! Please enter a numeric value.")
            continue  # Go back to menu

        # Perform the correct conversion based on choice
        if choice == '1':
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C = {result}°F")

        elif choice == '2':
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F = {result}°C")

        elif choice == '3':
            result = celsius_to_kelvin(temp)
            print(f"{temp}°C = {result}K")

        elif choice == '4':
            result = kelvin_to_celsius(temp)
            print(f"{temp}K = {result}°C")

        elif choice == '5':
            result = fahrenheit_to_kelvin(temp)
            print(f"{temp}°F = {result}K")

        elif choice == '6':
            result = kelvin_to_fahrenheit(temp)
            print(f"{temp}K = {result}°F")

    else:
        # If user enters something outside 1-7
        print("Invalid option! Please choose between 1 and 7.")
