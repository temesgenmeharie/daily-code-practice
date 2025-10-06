# Day 5: List and Loop Practice
# Author: Temesgen Meharie
# Goal: Practice list operations, loops, and basic functions

def analyze_numbers(numbers):
    print("\nNumbers:", numbers)
    print("Sum:", sum(numbers))
    print("Max:", max(numbers))
    print("Min:", min(numbers))
    print("Average:", sum(numbers) / len(numbers))
    print("Ascending:", sorted(numbers))
    print("Descending:", sorted(numbers, reverse=True))


def main():
    numbers = []
    print("Enter 5 numbers:")

    for i in range(5):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)

    analyze_numbers(numbers)


if __name__ == "__main__":
    main()
