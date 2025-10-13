# ======================================
# Day 11 - Loops + Lists + Dictionaries
# Each task is clearly separated
# Comments explain every line
# ======================================

# --------------------------------------
# Task 1: Print multiplication table (1 to 10)
# --------------------------------------
print("Task 1: Multiplication Table (1 to 10)")
for i in range(1, 11):  # Outer loop for the first number
    for j in range(1, 11):  # Inner loop for the second number
        print(f"{i} x {j} = {i * j}")
    print("-" * 20)  # Separator after each row

# --------------------------------------
# Task 2: Print only even numbers from 1–50
# --------------------------------------
print("\nTask 2: Even numbers from 1 to 50")
for num in range(1, 51):
    if num % 2 == 0:  # Check if divisible by 2
        print(num, end=" ")
print()  # New line

# --------------------------------------
# Task 3: Sum of all numbers in a list
# --------------------------------------
print("\nTask 3: Sum of list")
numbers = [10, 20, 30, 40]
total = 0
for n in numbers:
    total += n  # Add each number to total
print("List:", numbers)
print("Sum =", total)

# --------------------------------------
# Task 4: Find largest number in list (WITHOUT max())
# --------------------------------------
print("\nTask 4: Find largest number")
nums = [4, 9, 2, 7, 5]
largest = nums[0]  # Assume the first number is the largest
for n in nums:
    if n > largest:
        largest = n  # Update largest if found bigger
print("List:", nums)
print("Largest number =", largest)

# --------------------------------------
# Task 5: Count how many times a word appears in a sentence
# --------------------------------------
print("\nTask 5: Count word frequency")
sentence = "I love python because python is easy"
word = "python"
count = 0
for w in sentence.split():  # Split sentence into words
    if w.lower() == word.lower():  # Case insensitive
        count += 1
print("Sentence:", sentence)
print(f"'{word}' appears {count} times")

# --------------------------------------
# Task 6: Remove duplicates from a list
# --------------------------------------
print("\nTask 6: Remove duplicates")
dup_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for item in dup_list:
    if item not in unique_list:
        unique_list.append(item)  # Add only if not already in list
print("Original:", dup_list)
print("Without duplicates:", unique_list)

# --------------------------------------
# Task 7: Loop through a dictionary and print key → value
# --------------------------------------
print("\nTask 7: Loop dictionary")
person = {"name": "Temesgen", "age": 23, "city": "Arba Minch"}
for key, value in person.items():
    print(f"{key} : {value}")

# --------------------------------------
# Task 8: Use break and continue
# --------------------------------------
print("\nTask 8: break and continue")
for i in range(1, 11):
    if i == 5:
        continue  # Skip 5
    if i == 8:
        break  # Stop at 8
    print(i)

# --------------------------------------
# BONUS CHALLENGE: ATM PIN System
# --------------------------------------
print("\nBONUS: ATM PIN System")
correct_pin = "1234"
attempts = 3

while attempts > 0:
    user_pin = input("Enter your PIN: ")
    
    if user_pin == correct_pin:
        print("Access Granted ✅")
        break
    else:
        attempts -= 1
        print(f"Wrong PIN! Attempts left: {attempts}")

if attempts == 0:
    print("Account Locked ❌")
