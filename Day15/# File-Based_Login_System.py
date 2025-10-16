# -------------------------------
# File-Based Login System
# -------------------------------

def register_user():
    """
    Registers a new user by saving username and password to a file
    """
    try:
        username = input("Enter new username: ").strip()
        password = input("Enter new password: ").strip()

        if username == "" or password == "":
            raise ValueError("Username or password cannot be empty!")

        # Check if username already exists
        with open("users.txt", "r") as file:
            for line in file:
                stored_username = line.strip().split(",")[0]
                if username == stored_username:
                    raise ValueError("Username already exists!")

        # Append new user to file
        with open("users.txt", "a") as file:
            file.write(f"{username},{password}\n")

        print("✅ Registration successful!")

    except FileNotFoundError:
        # If users.txt does not exist, create it and register first user
        with open("users.txt", "w") as file:
            file.write(f"{username},{password}\n")
        print("✅ Registration successful! (File created)")

    except ValueError as ve:
        print("Error:", ve)

    finally:
        print("Registration attempt finished.\n")


def login_user():
    """
    Logs in a user by checking credentials from the file
    """
    attempts = 3
    while attempts > 0:
        try:
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()

            if username == "" or password == "":
                raise ValueError("Username or password cannot be empty!")

            found = False
            with open("users.txt", "r") as file:
                for line in file:
                    stored_username, stored_password = line.strip().split(",")
                    if username == stored_username and password == stored_password:
                        found = True
                        break

            if not found:
                raise ValueError("Incorrect username or password!")

        except FileNotFoundError:
            print("No users registered yet. Please register first.")
            return

        except ValueError as ve:
            print("Login Error:", ve)
            attempts -= 1
            print(f"Attempts left: {attempts}")

        else:
            print("✅ Login successful! Welcome,", username)
            break

        finally:
            print("Login attempt finished.\n")

    if attempts == 0:
        print("❌ Too many failed login attempts. Access denied.")


# -------------------------------
# Main Menu
# -------------------------------
while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
