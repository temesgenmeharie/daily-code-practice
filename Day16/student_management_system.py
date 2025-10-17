"""
Enhanced Student Management System
- Uses OOP (Student class + StudentManagementSystem manager)
- Input validation and error handling
- CRUD operations: add, view, search, remove, update
- Menu-driven CLI
"""

from typing import List, Optional  # typing helpers for clarity
import sys                         # to allow a clean program exit


# ----------------------------
# Student data model (class)
# ----------------------------
class Student:
    """Represents a student with basic attributes."""

    def __init__(self, name: str, student_id: str, grade: str, department: str):
        # Store provided values as attributes on the instance
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.department = department

    def to_dict(self) -> dict:
        """Return a dictionary representation (useful for future persistence)."""
        return {
            "name": self.name,
            "student_id": self.student_id,
            "grade": self.grade,
            "department": self.department
        }

    def display(self) -> None:
        """Print a single student's details in a readable format."""
        print(f"ID: {self.student_id} | Name: {self.name} | Grade: {self.grade} | Dept: {self.department}")


# ---------------------------------------
# Student Management System (manager)
# ---------------------------------------
class StudentManagementSystem:
    """Manages a list of Student objects and provides CRUD operations."""

    def __init__(self):
        # Initialize an empty list to hold Student objects
        self.students: List[Student] = []

    # ------------------------
    # Helper & validation
    # ------------------------
    def _find_index_by_id(self, student_id: str) -> Optional[int]:
        """
        Find the index of a student in the list by student_id.
        Returns the index if found, otherwise returns None.
        """
        for index, student in enumerate(self.students):
            if student.student_id == student_id:
                return index
        return None

    def _is_unique_id(self, student_id: str) -> bool:
        """Return True if no student has the given student_id."""
        return self._find_index_by_id(student_id) is None

    def _validate_non_empty(self, value: str, field_name: str) -> None:
        """
        Validate that a string value is not empty.
        Raises ValueError if validation fails.
        """
        if not value or value.strip() == "":
            raise ValueError(f"{field_name} cannot be empty.")

    # ------------------------
    # CRUD operations
    # ------------------------
    def add_student(self, name: str, student_id: str, grade: str, department: str) -> None:
        """
        Add a new student after validating inputs and checking for unique ID.
        Raises ValueError on invalid input or duplicate ID.
        """
        # Validate inputs (raise ValueError if any are invalid)
        self._validate_non_empty(name, "Name")
        self._validate_non_empty(student_id, "Student ID")
        self._validate_non_empty(grade, "Grade")
        self._validate_non_empty(department, "Department")

        # Check for unique student ID
        if not self._is_unique_id(student_id):
            raise ValueError(f"Student ID '{student_id}' already exists. Please use a unique ID.")

        # Create Student object and append to list
        new_student = Student(name.strip(), student_id.strip(), grade.strip(), department.strip())
        self.students.append(new_student)
        print(f"Student '{name}' (ID: {student_id}) added successfully.")

    def view_all_students(self) -> None:
        """Print all students in the system in a friendly table format."""
        if not self.students:
            print("No students found. Add students first.")
            return

        print("\n=== All Students ===")
        # Loop through each student and call display()
        for student in self.students:
            student.display()
        print("====================\n")

    def search_student(self, student_id: str) -> Optional[Student]:
        """
        Search for a student by ID.
        Returns the Student object if found, otherwise None.
        """
        idx = self._find_index_by_id(student_id)
        if idx is None:
            return None
        return self.students[idx]

    def remove_student(self, student_id: str) -> bool:
        """
        Remove a student by ID.
        Returns True if removal succeeded, False if not found.
        """
        idx = self._find_index_by_id(student_id)
        if idx is None:
            return False
        removed_student = self.students.pop(idx)
        print(f"Student '{removed_student.name}' (ID: {removed_student.student_id}) removed.")
        return True

    def update_student(self, student_id: str, name: Optional[str] = None,
                       grade: Optional[str] = None, department: Optional[str] = None) -> bool:
        """
        Update student details. Only non-None parameters are updated.
        Returns True if student found and updated, False if not found.
        """
        idx = self._find_index_by_id(student_id)
        if idx is None:
            return False

        student = self.students[idx]

        # Update fields only if new values provided (and not empty)
        if name is not None:
            self._validate_non_empty(name, "Name")
            student.name = name.strip()
        if grade is not None:
            self._validate_non_empty(grade, "Grade")
            student.grade = grade.strip()
        if department is not None:
            self._validate_non_empty(department, "Department")
            student.department = department.strip()

        print(f"Student (ID: {student_id}) updated successfully.")
        return True


# ----------------------------
# CLI: menu and user interaction
# ----------------------------
def main_menu():
    """Run the interactive command-line menu."""
    system = StudentManagementSystem()  # create manager instance

    # Loop until the user chooses to exit
    while True:
        # Display menu options
        print("=== Student Management System ===")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student by ID")
        print("4. Update student")
        print("5. Remove student")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        # Option 1: Add student
        if choice == "1":
            try:
                # Prompt user for details
                name = input("Enter student name: ")
                student_id = input("Enter student ID: ")
                grade = input("Enter grade (e.g., 10, A, B+): ")
                department = input("Enter department: ")
                # Try to add student (may raise ValueError)
                system.add_student(name, student_id, grade, department)
            except ValueError as ve:
                # Show friendly error message for invalid input
                print("Error adding student:", ve)
            except Exception as e:
                # Catch-all for unexpected errors (keep program stable)
                print("Unexpected error:", e)

        # Option 2: View all students
        elif choice == "2":
            system.view_all_students()

        # Option 3: Search by ID
        elif choice == "3":
            sid = input("Enter student ID to search: ").strip()
            if not sid:
                print("Student ID cannot be empty.")
                continue
            student = system.search_student(sid)
            if student:
                print("Student found:")
                student.display()
            else:
                print(f"No student found with ID: {sid}")

        # Option 4: Update student
        elif choice == "4":
            sid = input("Enter student ID to update: ").strip()
            if not sid:
                print("Student ID cannot be empty.")
                continue
            # Get new values; allow user to press Enter to skip a field
            print("Leave a field empty to keep current value.")
            new_name = input("New name (press Enter to skip): ")
            new_grade = input("New grade (press Enter to skip): ")
            new_department = input("New department (press Enter to skip): ")

            # Determine which fields to update (None means skip)
            update_name = new_name if new_name.strip() != "" else None
            update_grade = new_grade if new_grade.strip() != "" else None
            update_dept = new_department if new_department.strip() != "" else None

            try:
                updated = system.update_student(sid, name=update_name, grade=update_grade, department=update_dept)
                if not updated:
                    print(f"No student found with ID: {sid}")
            except ValueError as ve:
                print("Error updating student:", ve)

        # Option 5: Remove student
        elif choice == "5":
            sid = input("Enter student ID to remove: ").strip()
            if not sid:
                print("Student ID cannot be empty.")
                continue
            confirmed = input(f"Are you sure you want to delete student {sid}? (y/n): ").strip().lower()
            if confirmed == "y":
                removed = system.remove_student(sid)
                if not removed:
                    print(f"No student found with ID: {sid}")
            else:
                print("Delete cancelled.")

        # Option 6: Exit
        elif choice == "6":
            print("Exiting Student Management System. Goodbye!")
            sys.exit(0)  # clean exit

        # Invalid menu choice
        else:
            print("Invalid option. Please choose a number between 1 and 6.")

        # Small spacer for readability before showing menu again
        print()


# Run the menu if the script is executed directly
if __name__ == "__main__":
    main_menu()
