# ----------------------------------------------------------
# Day 9: Python Data Structures — Lists, Tuples, Dictionaries
# Author: Temesgen Meharie
# ----------------------------------------------------------

# 🧩 1. Working with Lists
print("==== 1. LISTS ====")

# Create a list of favorite programming languages
languages = ["Python", "JavaScript", "C++", "Java"]

# Print the list
print("Languages:", languages)

# Access items by index
print("First language:", languages[0])
print("Last language:", languages[-1])

# Add a new item
languages.append("Go")

# Remove an item
languages.remove("Java")

# Loop through the list
for lang in languages:
    print("I like", lang)

# Print total number of items
print("Total languages:", len(languages))

print("\n")


# 🧩 2. Working with Tuples
print("==== 2. TUPLES ====")

# Tuples are immutable (cannot be changed)
coordinates = (10, 20, 30)

# Access elements
print("X:", coordinates[0])
print("Y:", coordinates[1])
print("Z:", coordinates[2])

# Demonstrate immutability
print("Tuples are immutable — cannot modify their values directly.")
print("Tuple example:", coordinates)

print("\n")


# 🧩 3. Working with Dictionaries
print("==== 3. DICTIONARIES ====")

# Create a dictionary of student information
student = {
    "name": "Temesgen",
    "age": 22,
    "department": "Computer Science"
}

# Access values
print("Name:", student["name"])

# Add a new key-value pair
student["university"] = "Arba Minch University"

# Update existing value
student["age"] = 23

# Loop through dictionary items
for key, value in student.items():
    print(f"{key}: {value}")

# Check if a key exists
if "department" in student:
    print("Department key exists.")

print("\n")


# 🧩 4. Practice Section: Lists
print("==== 4. PRACTICE — LISTS ====")

fruits = ["apple", "banana", "mango", "orange"]
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Add and remove
fruits.append("grape")
fruits.remove("banana")
print("Updated fruits:", fruits)

# Loop in uppercase
for fruit in fruits:
    print(fruit.upper())

print("\n")


# 🧩 5. Practice Section: Tuples
print("==== 5. PRACTICE — TUPLES ====")

dimensions = (15, 25, 35)
print("Width:", dimensions[0])
print("Height:", dimensions[1])
print("Depth:", dimensions[2])
print("Tuples cannot be changed, only accessed.")

print("\n")


# 🧩 6. Practice Section: Dictionaries
print("==== 6. PRACTICE — DICTIONARIES ====")

student_info = {
    "name": "Temesgen",
    "age": 22,
    "skills": ["Python", "GitHub", "HTML"]
}
print("Name:", student_info["name"])
print("First skill:", student_info["skills"][0])

# Add and update
student_info["university"] = "Arba Minch University"
student_info["age"] = 23

for key, value in student_info.items():
    print(f"{key}: {value}")

print("\n")


# 🧩 7. Bonus Challenge — Combine Everything
print("==== 7. BONUS CHALLENGE ====")

students = [
    {"name": "Temesgen", "age": 23, "skills": ["Python", "GitHub"]},
    {"name": "Lidya", "age": 21, "skills": ["HTML", "CSS"]},
    {"name": "Samuel", "age": 22, "skills": ["C++", "Java"]}
]

for student in students:
    print(f"{student['name']} — First skill: {student['skills'][0]}")

print("\n🎉 Day 9 complete! Great job, Temesgen! 🚀")
