"""
Python Basics for Data Science
This script covers key Python skills: variables, strings, numbers, arithmetic, and conditionals.
Ideal for someone with some coding experience wanting to learn Python for data science.
"""

# -----------------------------
# Hello, Python! (Spam example)
# -----------------------------

# Variable assignment
spam_amount = 0
print("Initial spam amount:", spam_amount)

# Reassignment and arithmetic
spam_amount = spam_amount + 4  # Add 4 servings of spam
print("Updated spam amount:", spam_amount)

# Conditional statement: only print if spam_amount > 0
if spam_amount > 0:
    print("But I don't want ANY spam!")

# Strings and operator overloading: multiply a string by a number
viking_song = "Spam " * spam_amount
print("Viking song:", viking_song)

# -----------------------------
# Numbers and arithmetic
# -----------------------------

# Integers
print("Type of spam_amount:", type(spam_amount))  # int

# Floats
price = 19.95
print("Type of price:", type(price))  # float

# Arithmetic operations
a = 5
b = 2

print("Addition:", a + b)        # 7
print("Subtraction:", a - b)     # 3
print("Multiplication:", a * b)  # 10
print("True division:", a / b)   # 2.5 (always float)
print("Floor division:", a // b) # 2 (integer part)
print("Modulus:", a % b)         # 1 (remainder)
print("Exponentiation:", a ** b) # 25
print("Negation:", -a)           # -5

# Order of operations
print("8 - 3 + 2 =", 8 - 3 + 2)       # 7
print("-3 + 4 * 2 =", -3 + 4 * 2)     # 5

# Using parentheses to control order
hat_height_cm = 25
my_height_cm = 190
# Incorrect order
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters (wrong order):", total_height_meters)
# Correct order
total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters (correct):", total_height_meters)

# Built-in functions for numbers
print("Min of 1,2,3:", min(1, 2, 3))
print("Max of 1,2,3:", max(1, 2, 3))
print("Absolute value of 32:", abs(32))
print("Absolute value of -32:", abs(-32))

# Type conversions
print("Convert int to float:", float(10))       # 10.0
print("Convert float to int:", int(3.33))       # 3
print("Convert string to int:", int('807') + 1) # 808

# -----------------------------
# Summary
# -----------------------------
# This code demonstrates:
# - Variables and assignment
# - Strings and repetition with *
# - Conditional statements (if)
# - Integers and floats
# - Arithmetic operators
# - Operator precedence and parentheses
# - Built-in functions: type, min, max, abs, int, float
