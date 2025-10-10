# banking_system.py
# -----------------------------------------
# Console-Based Banking System (Advanced)
# Features:
# - Create account
# - Deposit money
# - Withdraw money
# - Check balance
# - Transaction history
# - Persistent storage using JSON file
# -----------------------------------------

import json       # For saving and loading accounts from a JSON file
import os         # For checking if the file exists

# --------------------------
# File to store accounts
# --------------------------
ACCOUNTS_FILE = "accounts.json"

# --------------------------
# Load existing accounts from file
# --------------------------
def load_accounts():
    """Load accounts from JSON file or return empty dict if file doesn't exist"""
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "r") as f:
            try:
                return json.load(f)  # Read JSON as dictionary
            except json.JSONDecodeError:
                return {}  # Return empty dict if JSON is corrupted
    else:
        return {}  # Return empty dict if file doesn't exist

# --------------------------
# Save accounts to file
# --------------------------
def save_accounts(accounts):
    """Save the accounts dictionary to JSON file"""
    with open(ACCOUNTS_FILE, "w") as f:
        json.dump(accounts, f, indent=4)  # indent=4 for readability

# --------------------------
# Generate a unique account number
# --------------------------
def generate_account_number(accounts):
    """Generate a new account number by incrementing the max existing account number"""
    if accounts:
        max_acc = max(int(acc) for acc in accounts.keys())
        return str(max_acc + 1)
    else:
        return "1001"  # Start from 1001 if no accounts exist

# --------------------------
# Create a new account
# --------------------------
def create_account(accounts):
    """Create a new account with name and initial deposit"""
    name = input("Enter account holder's name: ").strip()
    while True:
        try:
            initial_deposit = float(input("Enter initial deposit: "))
            if initial_deposit < 0:
                print("Deposit must be non-negative!")
                continue
            break
        except ValueError:
            print("Please enter a valid number for deposit.")

    acc_num = generate_account_number(accounts)
    accounts[acc_num] = {
        "name": name,
        "balance": initial_deposit,
        "transactions": [f"Initial deposit: {initial_deposit}"]
    }
    save_accounts(accounts)
    print(f"Account created successfully! Account Number: {acc_num}")

# --------------------------
# Deposit money
# --------------------------
def deposit(accounts):
    acc_num = input("Enter account number: ").strip()
    if acc_num not in accounts:
        print("Account not found!")
        return

    while True:
        try:
            amount = float(input("Enter deposit amount: "))
            if amount <= 0:
                print("Amount must be greater than 0!")
                continue
            break
        except ValueError:
            print("Enter a valid number!")

    accounts[acc_num]["balance"] += amount
    accounts[acc_num]["transactions"].append(f"Deposited: {amount}")
    save_accounts(accounts)
    print(f"Deposited {amount} successfully! New balance: {accounts[acc_num]['balance']}")

# --------------------------
# Withdraw money
# --------------------------
def withdraw(accounts):
    acc_num = input("Enter account number: ").strip()
    if acc_num not in accounts:
        print("Account not found!")
        return

    while True:
        try:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Amount must be greater than 0!")
                continue
            if amount > accounts[acc_num]["balance"]:
                print("Insufficient balance!")
                continue
            break
        except ValueError:
            print("Enter a valid number!")

    accounts[acc_num]["balance"] -= amount
    accounts[acc_num]["transactions"].append(f"Withdrew: {amount}")
    save_accounts(accounts)
    print(f"Withdrew {amount} successfully! New balance: {accounts[acc_num]['balance']}")

# --------------------------
# Check balance
# --------------------------
def check_balance(accounts):
    acc_num = input("Enter account number: ").strip()
    if acc_num not in accounts:
        print("Account not found!")
        return
    balance = accounts[acc_num]["balance"]
    print(f"Account Balance for {accounts[acc_num]['name']} ({acc_num}): {balance}")

# --------------------------
# View transaction history
# --------------------------
def view_transactions(accounts):
    acc_num = input("Enter account number: ").strip()
    if acc_num not in accounts:
        print("Account not found!")
        return
    print(f"Transaction History for {accounts[acc_num]['name']} ({acc_num}):")
    for t in accounts[acc_num]["transactions"]:
        print("-", t)

# --------------------------
# Main program loop
# --------------------------
def main():
    accounts = load_accounts()  # Load accounts at the start
    while True:
        print("\n=== Welcome to Selam Bank ===")
        print("1. Create new account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. View transaction history")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()
        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit(accounts)
        elif choice == "3":
            withdraw(accounts)
        elif choice == "4":
            check_balance(accounts)
        elif choice == "5":
            view_transactions(accounts)
        elif choice == "6":
            print("Thank you for using Selam Bank. Goodbye!")
            break
        else:
            print("Invalid option! Please choose between 1 and 6.")

# --------------------------
# Run the program
# --------------------------
if __name__ == "__main__":
    main()
