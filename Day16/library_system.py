"""
library_system.py
Professional Library Management System
- OOP: Book, User, Library classes
- File persistence using JSON
- Exception handling for robust behavior
- Interactive menu for librarians/users
"""

import json                # to save/load data in JSON format
import os                  # to check for file existence
import datetime            # to record borrow timestamps
from typing import Dict, Optional, List

# -------------------------
# File names for persistence
# -------------------------
BOOKS_FILE = "books.json"   # stores book records
USERS_FILE = "users.json"   # stores registered users

# -------------------------
# Helper functions
# -------------------------
def read_json_file(filename: str) -> Dict:
    """
    Read JSON data from filename. If file doesn't exist, return empty dict.
    If file is invalid JSON, raise ValueError.
    """
    if not os.path.exists(filename):
        # No file yet — return empty dictionary (we'll create file when saving)
        return {}
    with open(filename, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # File exists but invalid JSON — raise so caller can handle
            raise ValueError(f"Corrupted JSON in {filename}.")

def write_json_file(filename: str, data: Dict) -> None:
    """
    Write dictionary data to filename in JSON format (pretty printed).
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# -------------------------
# Book class (OOP model)
# -------------------------
class Book:
    """
    Represents a book in the library.
    Each book has a unique book_id (string), title, author, year, and borrowed info.
    borrowed_by: None or user_id of borrower
    borrowed_at: None or ISO timestamp string when borrowed
    """
    def __init__(self, book_id: str, title: str, author: str, year: int):
        self.book_id = book_id            # unique book identifier
        self.title = title                # book title
        self.author = author              # book author
        self.year = year                  # publication year
        self.borrowed_by: Optional[str] = None   # user_id if borrowed otherwise None
        self.borrowed_at: Optional[str] = None   # ISO timestamp string if borrowed

    def to_dict(self) -> Dict:
        """
        Return a JSON-serializable dict representation of the book.
        """
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "borrowed_by": self.borrowed_by,
            "borrowed_at": self.borrowed_at
        }

    @staticmethod
    def from_dict(data: Dict):
        """
        Create a Book object from a dictionary (used when loading from file).
        """
        b = Book(str(data["book_id"]), data["title"], data["author"], int(data["year"]))
        b.borrowed_by = data.get("borrowed_by")
        b.borrowed_at = data.get("borrowed_at")
        return b

    def is_available(self) -> bool:
        """Return True if book is not currently borrowed."""
        return self.borrowed_by is None

    def borrow(self, user_id: str) -> None:
        """
        Mark the book as borrowed by user_id and set borrowed_at timestamp.
        Raises ValueError if already borrowed.
        """
        if not self.is_available():
            raise ValueError(f"Book '{self.title}' is already borrowed by user {self.borrowed_by}.")
        self.borrowed_by = user_id
        self.borrowed_at = datetime.datetime.now().isoformat()

    def returned(self) -> None:
        """
        Mark the book as returned (clear borrowed_by and borrowed_at).
        """
        self.borrowed_by = None
        self.borrowed_at = None


# -------------------------
# User class (OOP model)
# -------------------------
class User:
    """
    Represents a library user (student or member).
    Attributes: user_id (string), name, email (optional), registered_at timestamp.
    """
    def __init__(self, user_id: str, name: str, email: Optional[str] = None):
        self.user_id = user_id                  # unique user identifier
        self.name = name                        # user's full name
        self.email = email                      # optional email
        self.registered_at = datetime.datetime.now().isoformat()  # registration time

    def to_dict(self) -> Dict:
        """Return a JSON-serializable dict for the user."""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "registered_at": self.registered_at
        }

    @staticmethod
    def from_dict(data: Dict):
        """Construct a User from a dict."""
        u = User(str(data["user_id"]), data["name"], data.get("email"))
        u.registered_at = data.get("registered_at", u.registered_at)
        return u


# -------------------------
# Library manager (core)
# -------------------------
class Library:
    """
    Manages books and users, handles persistence and business logic.
    Books and users are stored in dictionaries keyed by their IDs.
    """
    def __init__(self):
        # load persisted data (or start empty)
        self.books: Dict[str, Book] = {}  # book_id -> Book
        self.users: Dict[str, User] = {}  # user_id -> User
        # try to load saved data from JSON files
        self._load_data()

    # -------------------------
    # Persistence: load & save
    # -------------------------
    def _load_data(self) -> None:
        """
        Load books and users from JSON files.
        If files don't exist, starts with empty collections.
        If JSON is corrupted, shows an error and starts empty.
        """
        # Load books
        try:
            books_data = read_json_file(BOOKS_FILE)
            for bid, bdict in books_data.items():
                try:
                    self.books[bid] = Book.from_dict(bdict)
                except Exception:
                    # Skip malformed book entries
                    print(f"Warning: Skipping malformed book entry {bid}")
        except ValueError as ve:
            # JSON corrupted
            print("Warning:", ve)
            self.books = {}

        # Load users
        try:
            users_data = read_json_file(USERS_FILE)
            for uid, udict in users_data.items():
                try:
                    self.users[uid] = User.from_dict(udict)
                except Exception:
                    print(f"Warning: Skipping malformed user entry {uid}")
        except ValueError as ve:
            print("Warning:", ve)
            self.users = {}

    def _save_data(self) -> None:
        """
        Save current books and users to JSON files.
        Called after any change that should persist.
        """
        # Convert books dict to serializable dict
        books_out = {bid: book.to_dict() for bid, book in self.books.items()}
        write_json_file(BOOKS_FILE, books_out)

        # Convert users dict to serializable dict
        users_out = {uid: user.to_dict() for uid, user in self.users.items()}
        write_json_file(USERS_FILE, users_out)

    # -------------------------
    # Book management
    # -------------------------
    def add_book(self, book_id: str, title: str, author: str, year: int) -> None:
        """
        Add a new book to the library.
        Raises ValueError if book_id already exists or invalid inputs.
        """
        if not book_id or not title or not author:
            raise ValueError("Book ID, title, and author are required.")
        if str(book_id) in self.books:
            raise ValueError(f"Book ID '{book_id}' already exists.")
        # create Book object and store
        book = Book(str(book_id), title.strip(), author.strip(), int(year))
        self.books[book.book_id] = book
        # persist changes
        self._save_data()

    def view_all_books(self) -> List[Dict]:
        """
        Return a list of dictionaries describing each book for display.
        """
        result = []
        for book in self.books.values():
            status = "Available" if book.is_available() else f"Borrowed by {book.borrowed_by}"
            result.append({
                "book_id": book.book_id,
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "status": status,
                "borrowed_at": book.borrowed_at
            })
        return result

    def search_books(self, query: str) -> List[Dict]:
        """
        Search for books by title or author (case-insensitive substring match).
        Returns matching book dicts.
        """
        q = query.strip().lower()
        matches = []
        for book in self.books.values():
            if q in book.title.lower() or q in book.author.lower():
                matches.append(book.to_dict())
        return matches

    # -------------------------
    # User management
    # -------------------------
    def register_user(self, user_id: str, name: str, email: Optional[str] = None) -> None:
        """
        Register a new user.
        Raises ValueError on invalid input or duplicate ID.
        """
        if not user_id or not name:
            raise ValueError("User ID and name are required.")
        if user_id in self.users:
            raise ValueError(f"User ID '{user_id}' already registered.")
        user = User(str(user_id), name.strip(), email.strip() if email else None)
        self.users[user.user_id] = user
        self._save_data()

    def view_all_users(self) -> List[Dict]:
        """
        Return list of user dicts for display.
        """
        return [user.to_dict() for user in self.users.values()]

    # -------------------------
    # Borrow / Return business logic
    # -------------------------
    def borrow_book(self, user_id: str, book_id: str) -> None:
        """
        Borrow a book: checks that user & book exist and book is available.
        Raises ValueError when rules are violated.
        """
        if user_id not in self.users:
            raise ValueError("User not registered.")
        if book_id not in self.books:
            raise ValueError("Book not found.")
        book = self.books[book_id]
        if not book.is_available():
            raise ValueError(f"Book already borrowed by user {book.borrowed_by}.")
        # perform borrow
        book.borrow(user_id)
        # persist
        self._save_data()

    def return_book(self, user_id: str, book_id: str) -> None:
        """
        Return a book: checks that book exists and is currently borrowed by the user.
        """
        if book_id not in self.books:
            raise ValueError("Book not found.")
        book = self.books[book_id]
        if book.is_available():
            raise ValueError("Book is not currently borrowed.")
        if book.borrowed_by != user_id:
            raise ValueError("This book was not borrowed by this user.")
        # perform return
        book.returned()
        # persist
        self._save_data()

    def user_borrowed_books(self, user_id: str) -> List[Dict]:
        """
        Return list of books currently borrowed by the specified user.
        """
        borrowed = []
        for b in self.books.values():
            if b.borrowed_by == user_id:
                borrowed.append(b.to_dict())
        return borrowed


# -------------------------
# CLI: interactive menu
# -------------------------
def main_menu():
    """
    Command-line interface for the library system.
    Handles user input and calls Library class methods with exception handling.
    """
    lib = Library()  # create library manager (loads existing data if present)

    # Helper to print a divider
    def divider():
        print("\n" + "-" * 50 + "\n")

    print("Welcome to the Library Management System")
    while True:
        # Print menu options
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Books (title/author)")
        print("4. Register User")
        print("5. View All Users")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. View My Borrowed Books")
        print("9. Exit")

        choice = input("Select an option (1-9): ").strip()

        # Option 1: Add Book
        if choice == "1":
            try:
                bid = input("Enter book ID: ").strip()
                title = input("Enter title: ").strip()
                author = input("Enter author: ").strip()
                year_input = input("Enter publication year (e.g., 2020): ").strip()
                if not year_input.isdigit():
                    raise ValueError("Year must be a number.")
                year = int(year_input)
                lib.add_book(bid, title, author, year)
                print("Book added successfully.")
            except ValueError as ve:
                print("Error:", ve)

        # Option 2: View All Books
        elif choice == "2":
            books = lib.view_all_books()
            if not books:
                print("No books found.")
            else:
                print("Books in library:")
                for b in books:
                    status = b["status"]
                    borrowed_at = b.get("borrowed_at")
                    line = f"{b['book_id']} | {b['title']} by {b['author']} ({b['year']}) -- {status}"
                    if borrowed_at:
                        line += f" at {borrowed_at}"
                    print(line)

        # Option 3: Search Books
        elif choice == "3":
            q = input("Enter search query (title or author): ").strip()
            if not q:
                print("Please enter a search query.")
            else:
                matches = lib.search_books(q)
                if not matches:
                    print("No matches found.")
                else:
                    print(f"Found {len(matches)} match(es):")
                    for m in matches:
                        borrowed_by = m.get("borrowed_by")
                        status = "Available" if not borrowed_by else f"Borrowed by {borrowed_by}"
                        print(f"{m['book_id']} | {m['title']} by {m['author']} ({m['year']}) -- {status}")

        # Option 4: Register User
        elif choice == "4":
            try:
                uid = input("Enter user ID: ").strip()
                name = input("Enter full name: ").strip()
                email = input("Enter email (optional): ").strip()
                email = email if email else None
                lib.register_user(uid, name, email)
                print("User registered successfully.")
            except ValueError as ve:
                print("Error:", ve)

        # Option 5: View All Users
        elif choice == "5":
            users = lib.view_all_users()
            if not users:
                print("No users registered.")
            else:
                print("Registered users:")
                for u in users:
                    print(f"{u['user_id']} | {u['name']} (email: {u.get('email')})")

        # Option 6: Borrow Book
        elif choice == "6":
            try:
                uid = input("Enter your user ID: ").strip()
                bid = input("Enter book ID to borrow: ").strip()
                lib.borrow_book(uid, bid)
                print("Book borrowed successfully.")
            except ValueError as ve:
                print("Error:", ve)

        # Option 7: Return Book
        elif choice == "7":
            try:
                uid = input("Enter your user ID: ").strip()
                bid = input("Enter book ID to return: ").strip()
                lib.return_book(uid, bid)
                print("Book returned successfully.")
            except ValueError as ve:
                print("Error:", ve)

        # Option 8: View My Borrowed Books
        elif choice == "8":
            uid = input("Enter your user ID: ").strip()
            borrowed = lib.user_borrowed_books(uid)
            if not borrowed:
                print("No borrowed books found for this user.")
            else:
                print(f"Books borrowed by {uid}:")
                for b in borrowed:
                    print(f"{b['book_id']} | {b['title']} (borrowed at {b['borrowed_at']})")

        # Option 9: Exit
        elif choice == "9":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")

        divider()


# Run the program when executed directly
if __name__ == "__main__":
    main_menu()
