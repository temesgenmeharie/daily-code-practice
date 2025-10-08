# ------------------------------------------
# 🧾 Daily Expense Tracker
# Concepts used: File Handling, Functions, Error Handling, Dictionaries
# ------------------------------------------

# Define a function to add a new expense entry
def add_expense(file_name, category, amount):
    try:
        # Open the file in 'append' mode ('a') to add data without deleting previous entries
        with open(file_name, 'a') as f:
            # Write the expense details (category and amount) separated by a comma
            f.write(f"{category},{amount}\n")
        # Print confirmation message when expense is successfully recorded
        print("✅ Expense recorded successfully.")
    
    # Catch and handle any error that occurs while writing to the file
    except Exception as e:
        print("⚠️ Error writing to file:", e)


# Define a function to show the total expenses by category
def show_summary(file_name):
    # Create an empty dictionary to store total expenses per category
    expenses = {}
    
    try:
        # Open the file in read mode ('r') to read all recorded expenses
        with open(file_name, 'r') as f:
            # Loop through each line in the file
            for line in f:
                # Remove any extra spaces or newline characters, then split by comma
                category, amount = line.strip().split(',')
                # Convert amount from string to float and add it to the correct category
                expenses[category] = expenses.get(category, 0) + float(amount)
        
        # Print the final summary of all expenses grouped by category
        print("\n💰 Expense Summary:")
        for category, total in expenses.items():
            print(f"  - {category}: {total} birr")
    
    # Handle the case where the file does not exist
    except FileNotFoundError:
        print("⚠️ No expense records found. Please add some expenses first.")
    
    # Handle any other general error
    except Exception as e:
        print("⚠️ Error reading file:", e)


# ------------------------------------------
# 🧪 Example usage of the functions
# ------------------------------------------

# Add a few sample expenses
add_expense("expenses.txt", "Food", 50)
add_expense("expenses.txt", "Transport", 30)
add_expense("expenses.txt", "Groceries", 120)
add_expense("expenses.txt", "Food", 70)

# Display the total summary of expenses
show_summary("expenses.txt")
