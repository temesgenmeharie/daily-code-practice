# -------------------------------
# 🗒️ Personal Notes Manager
# -------------------------------

# This program helps users store and read personal notes from a file.
# It demonstrates file handling (read, write, append) and error handling.

NOTES_FILE = "notes.txt"

def add_note():
    note = input("Enter your note: ")
    with open(NOTES_FILE, "a") as file:
        file.write(note + "\n")
    print("✅ Note added successfully!\n")

def view_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            notes = file.readlines()
            if notes:
                print("\n📝 Your Notes:")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note.strip()}")
            else:
                print("No notes found.\n")
    except FileNotFoundError:
        print("⚠️ No notes file found. Add a note first!\n")

def delete_notes():
    confirm = input("Are you sure you want to delete all notes? (y/n): ")
    if confirm.lower() == "y":
        open(NOTES_FILE, "w").close()  # Clears the file content
        print("🗑️ All notes deleted!\n")

def menu():
    while True:
        print("\n========= Notes Manager =========")
        print("1️⃣ Add Note")
        print("2️⃣ View Notes")
        print("3️⃣ Delete All Notes")
        print("4️⃣ Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option! Please try again.\n")

# Run the Notes Manager
menu()
