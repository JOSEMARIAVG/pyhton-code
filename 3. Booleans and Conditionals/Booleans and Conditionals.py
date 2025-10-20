"""
Python Booleans and Conditionals
This script covers:
- Boolean type (True/False)
- Comparison operators
- Boolean operators (and, or, not)
- Conditional statements (if, elif, else)
- Boolean conversion with bool()
"""

# -----------------------------
# Boolean variables
# -----------------------------
x = True
print(x)           # True
print(type(x))     # <class 'bool'>

# -----------------------------
# Comparison operations
# -----------------------------
def can_run_for_president(age):
    """Can someone of the given age run for president in the US?"""
    # US Constitution: must be at least 35 years old
    return age >= 35

print("Can a 19-year-old run for president?", can_run_for_president(19))  # False
print("Can a 45-year-old run for president?", can_run_for_president(45))  # True

# Comparisons
print(3.0 == 3)  # True
print('3' == 3)  # False

# Check if a number is odd
def is_odd(n):
    return (n % 2) == 1

print("Is 100 odd?", is_odd(100))  # False
print("Is -1 odd?", is_odd(-1))    # True

# -----------------------------
# Combining boolean values
# -----------------------------
def can_run_for_president(age, is_natural_born_citizen):
    """Check age and citizenship requirements"""
    return is_natural_born_citizen and (age >= 35)

print(can_run_for_president(19, True))  # False
print(can_run_for_president(55, False)) # False
print(can_run_for_president(55, True))  # True

# Boolean operator precedence
print(True or True and False)  # True, because 'and' evaluated first

# Safe usage with parentheses
have_umbrella = False
rain_level = 3
have_hood = True
is_workday = True

prepared_for_weather = (
    have_umbrella 
    or ((rain_level < 5) and have_hood) 
    or (not (rain_level > 0 and is_workday))
)
print("Prepared for weather?", prepared_for_weather)

# -----------------------------
# Conditionals (if, elif, else)
# -----------------------------
def inspect(x):
    """Print if a number is zero, positive, or negative"""
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")

inspect(0)    # 0 is zero
inspect(-15)  # -15 is negative

# Indentation matters
def f(x):
    if x > 0:
        print("Only printed when x is positive; x =", x)
        print("Also only printed when x is positive; x =", x)
    print("Always printed, regardless of x's value; x =", x)

f(1)
f(0)

# -----------------------------
# Boolean conversion
# -----------------------------
print(bool(1))     # True, any non-zero number
print(bool(0))     # False
print(bool("asf")) # True, non-empty string
print(bool(""))    # False

# Non-boolean objects in conditions
if 0:
    print(0)       # Not printed, 0 is False
elif "spam":
    print("spam")  # Printed, non-empty string is True
