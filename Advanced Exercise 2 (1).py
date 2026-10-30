# -------------------------------------------
# Advanced Python Challenge: Exercise 02 Operators and Conditionals

# ----------------------------------------

# Overview:
# This exercise challenges your understanding of Python operators, conditionals, and input handling.
# Complete each section with the required logic, using good variable names and adding comments where necessary.

# -------------------------------------------
# Question 1: Multi-Step Arithmetic Operations
# -------------------------------------------

# Task:
# Use compound arithmetic operators to modify values of a, b, and c.
# Then calculate the square root of the sum of their squares.
# Tip: Use the math module.

import math

# Start with some base values
a = 5
b = 10
c = 7

# TODO: Add 3 to a using +=
a += 3
# TODO: Multiply b by 2 using *=
b *= 2
# TODO: Modulo c by 4 using %=
c %= 4

# TODO: Calculate the square root of (a^2 + b^2 + c^2)
result = math.hypot(a, b, c)
# TODO: Print the final result rounded to 2 decimal places
print(f"Final result: {result:.2f}")


# -------------------------------------------
# Question 2: Complex Conditional Evaluation
# -------------------------------------------

# Task:
# Ask the user to input three integers (x, y, z).
# Then evaluate and print whether:
# - x is even
# - y is positive
# - z is between 10 and 50
# Use logical operators to combine the conditions.

# Tip: Use and/or to join conditions.

# TODO: Input x, y, z
x = int(input("Enter the first integer (x): "))
y = int(input("Enter the second integer (y): "))
z = int(input("Enter the third integer (z): "))
# TODO: Create conditions:
#   is_even = True if x is even
is_even = x % 2 == 0
# is_positive = True if y > 0
is_positive = y > 0
#   is_in_range = True if z between 10 and 50
is_in_range = 10 <= z <= 50
# TODO: Create final_condition = is_even and is_positive and is_in_range
final_condition = is_even and is_positive and is_in_range
# TODO: Print final_condition
print(f"Final condition: {final_condition}")


# -------------------------------------------
# Question 3: Grading with Adjustments
# -------------------------------------------

# Task:
# Ask the user for their base score, then apply:
# - bonus points (+5)
# - late penalty (-10)
# Final score must not exceed 100 or drop below 0.
# Then assign a grade.

# Tip: Use min() and max() to constrain the score.

# TODO: Input score from user
base_score = float(input("Enter your base score: "))
# TODO: Apply adjustments
adjusted_score = base_score + 5 - 10
# TODO: Clamp score between 0 and 100
final_score = max(0, min(100, adjusted_score))
# TODO: Use if-elif-else to determine grade and print it
if final_score >= 80:
    grade = "A"
elif final_score >= 70:
    grade = "B"
elif final_score >= 60:
    grade = "C"
else:
    grade = "D"
print(f"Your final score is {final_score:.2f} and your grade is {grade}.")

# Handle division/modulus by zero with error checking.
# Perform the operation and print the result.

# Tip: Use try-except and elif branches for each operation.

# TODO: Input num1, num2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# TODO: Input operation
operation = input("Enter the operation (+, -, *, /, %, **): ")
# TODO: Match operation using if-elif
# TODO: Handle division/modulus by zero with try-except
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        result = None
elif operation == '%':
    try:
        result = num1 % num2
    except ZeroDivisionError:
        print("Error: Modulus by zero is not allowed.")
        result = None
elif operation == '**':
    result = num1 ** num2
# TODO: Print result
if result is not None:
    print(f"Result: {result}")
