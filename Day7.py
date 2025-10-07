# ------------------------------------------
# Day 7: File Handling Practice
# Author: Temesgen Meharie
# Description:
# This program allows the user to enter their name and message,
# saves it into a text file called 'messages.txt', and then
# reads and displays all saved messages.
# ------------------------------------------

# Function to save a message into the file
def save_message(name, message):
    """
    Saves a new message to messages.txt.
    The 'a' mode means append — it adds new lines without deleting old ones.
    """
    with open("messages.txt", "a") as file:
        file.write(f"{name}: {message}\n")  # Write name and message in one line


# Function to read all messages from the file
def read_messages():
    """
    Reads all messages from messages.txt and displays them.
    If the file does not exist yet, it shows a friendly message.
    """
    try:
        with open("messages.txt", "r") as file:
            messages = file.readlines()  # Read all lines as a list
            if len(messages) == 0:
                print("\nNo messages found yet.")
            else:
                print("\n--- All Messages ---")
                for msg in messages:
                    print(msg.strip())  # Remove extra newline characters
                print(f"\nTotal messages: {len(messages)}")
    except FileNotFoundError:
        print("\nNo message file found yet. Try adding a message first.")


# Main function — the main logic of the program
def main():
    print("=== Welcome to the Message Saver App ===")

    # Get user input
    name = input("Enter your name: ")
    message = input("Enter your message: ")

    # Save the user's message
    save_message(name, message)
    print("\n✅ Message saved successfully!")

    # Read and show all messages
    read_messages()


# Standard Python entry point
if __name__ == "__main__":
    main()
