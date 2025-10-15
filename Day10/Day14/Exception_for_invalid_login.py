# -------------------------------
# Custom Exception for invalid login
# -------------------------------
class LoginError(Exception):
    pass   # We don't need extra behavior, just a custom name


def login_system():
    # Predefined correct username and password
    CORRECT_USERNAME = "admin"
    CORRECT_PASSWORD = "12345"
    
    attempts = 3  # User can try 3 times

    while attempts > 0:
        try:
            # Ask user to enter username and password
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()

            # Check for empty input
            if username == "" or password == "":
                raise ValueError("Username or Password cannot be empty!")

            # Check if username is correct
            if username != CORRECT_USERNAME:
                raise LoginError("Invalid Username!")

            # Check if password is correct
            if password != CORRECT_PASSWORD:
                raise LoginError("Incorrect Password!")

        except ValueError as ve:
            # Handles empty input
            print("Input Error:", ve)

        except LoginError as le:
            # Handles wrong username or password
            print("Login Error:", le)
            attempts -= 1
            print(f"Attempts left: {attempts}")

        else:
            # Runs only if NO ERROR
            print("✅ Login Successful! Welcome!")
            break

        finally:
            # Always runs (can be used for logging or cleanup)
            print("Attempt finished.\n")

    # When attempts are over
    if attempts == 0:
        print("❌ Too many failed attempts. Access denied.")
