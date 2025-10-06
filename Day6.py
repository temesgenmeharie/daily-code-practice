# -------------------------------
# Day 6: Functions and Conditionals
# Author: Temesgen Meharie
# Description:
# This program asks the user for their age and determines
# their age group (Child, Teenager, Adult, Senior Citizen).
# It also checks if the age is even or odd using functions.
# -------------------------------

# Function to determine the age group
def check_age_group(age):
    """Return the age category based on the user's age."""
    if age < 0:
        return "Invalid age entered"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior Citizen"


# Function to check if age is even or odd
def check_even_or_odd(age):
    """Return whether the age is even or odd."""
    if age % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Main function — the starting point of the program
def main():
    # Ask the user for their age
    age = int(input("Enter your age: "))

    # Get the age group by calling the first function
    category = check_age_group(age)

    # Get whether the age is even or odd by calling the second function
    parity = check_even_or_odd(age)

    # Print results clearly
    print(f"\nYou are {age} years old.")
    print(f"Category: {category}")
    print(f"Your age is an {parity} number.")


# Run the main function when this file is executed
if __name__ == "__main__":
    main()
