"""
Python Functions for Data Science
This script covers:
- Using built-in functions
- Getting help with help()
- Defining your own functions
- Docstrings
- Return values
- Default arguments
- Functions as arguments (higher-order functions)
"""

# -----------------------------
# Using help() to explore functions
# -----------------------------
# Example with round()
help(round)  # Shows documentation for round function

# Pitfall: if you call the function first, help shows info about result, not the function itself
# help(round(-2.01))  # Shows help on -2, not round function

# Another example with print
help(print)  # Shows arguments: sep, end, file, flush

# -----------------------------
# Defining your own functions
# -----------------------------

# A function to find the smallest difference between any two numbers
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers among a, b, and c."""
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

# Test the function
print(
    least_difference(1, 10, 100),  # 9
    least_difference(1, 10, 10),   # 0
    least_difference(5, 6, 7),     # 1
)

# Check help and docstring
help(least_difference)

# -----------------------------
# Functions without return
# -----------------------------
def least_difference_no_return(a, b, c):
    """Function does calculation but does not return anything."""
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    min(diff1, diff2, diff3)  # No return

# Calling it returns None
print(
    least_difference_no_return(1, 10, 100),
    least_difference_no_return(1, 10, 10),
    least_difference_no_return(5, 6, 7),
)

# Using print as a function with side effect
mystery = print("Hello!")  # returns None
print("Value of mystery:", mystery)

# -----------------------------
# Default arguments
# -----------------------------
# print() has optional sep argument
print(1, 2, 3, sep=' < ')  # Custom separator
print(1, 2, 3)             # Default separator is space

# Defining functions with default arguments
def greet(who="Colin"):
    """Greet someone with a default name if not specified"""
    print("Hello,", who)

greet()             # Uses default
greet(who="Kaggle") # Uses keyword argument
greet("world")      # Positional argument

# -----------------------------
# Functions applied to functions (higher-order functions)
# -----------------------------
# Example: function that multiplies by 5
def mult_by_five(x):
    return 5 * x

# Call a function on an argument
def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

# Call a function on the result of a function
def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

# Testing higher-order functions
print(
    call(mult_by_five, 1),      # 5
    squared_call(mult_by_five, 1),  # 25
    sep='\n'
)

# -----------------------------
# Example using key argument in built-in max()
# -----------------------------
def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?', max(100, 51, 14),
    'Which number is the biggest modulo 5?', max(100, 51, 14, key=mod_5),
    sep='\n'
)
