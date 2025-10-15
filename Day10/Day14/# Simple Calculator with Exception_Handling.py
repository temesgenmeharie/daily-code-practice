# Simple Calculator with Exception Handling

def calculator():
    try:
        # Ask user for the first number
        num1 = float(input("Enter first number: "))
        
        # Ask user for the second number
        num2 = float(input("Enter second number: "))
        
        # Ask user to choose an operation
        print("Choose operation: +, -, *, /")
        op = input("Enter operator: ")

        # Perform operation using if-else
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            # This can cause ZeroDivisionError
            result = num1 / num2
        else:
            # If the operator is not valid, raise custom error
            raise ValueError("Invalid operator!")

    except ValueError:
        # This runs when input is not a valid number or invalid operator
        print("Error: Please enter valid numbers or operator.")
    
    except ZeroDivisionError:
        # This handles division by zero
        print("Error: Cannot divide by zero.")
    
    else:
        # Runs only if no exception occurred
        print("Result =", result)
    
    finally:
        # Always runs (cleanup or end message)
        print("Calculation complete!")


# Run the function
calculator()
