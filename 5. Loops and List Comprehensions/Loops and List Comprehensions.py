"""
Python Loops and List Comprehensions
This script covers:
- for loops
- while loops
- range()
- list comprehensions
"""

# -----------------------------
# For loops over a list
# -----------------------------
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

print("For loop over planets:")
for planet in planets:
    print(planet, end=' ')  # all on same line
print("\n")

# -----------------------------
# For loops over tuples
# -----------------------------
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
print("Product of tuple elements:", product)

# -----------------------------
# For loops over strings
# -----------------------------
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
print("Uppercase letters in string:")
for char in s:
    if char.isupper():
        print(char, end='')  # prints only uppercase letters
print("\n")

# -----------------------------
# range() function
# -----------------------------
print("Using range() in a for loop:")
for i in range(5):  # 0 to 4
    print("Doing important work. i =", i)

# -----------------------------
# while loops
# -----------------------------
print("\nWhile loop example:")
i = 0
while i < 10:
    print(i, end=' ')
    i += 1  # increment i
print("\n")

# -----------------------------
# List comprehensions
# -----------------------------
# squares from 0 to 9
squares = [n**2 for n in range(10)]
print("Squares using list comprehension:", squares)

# same without comprehension
squares2 = []
for n in range(10):
    squares2.append(n**2)
print("Squares using for loop:", squares2)

# filtering: planets with short names (<6 letters)
short_planets = [planet for planet in planets if len(planet) < 6]
print("Short planets:", short_planets)

# filtering + transformation: uppercase + '!'
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print("Loud short planets:", loud_short_planets)

# breaking it into multiple lines for readability
loud_short_planets_multiline = [
    planet.upper() + '!' 
    for planet in planets 
    if len(planet) < 6
]
print("Multiline comprehension:", loud_short_planets_multiline)

# constant expression in comprehension
constant_list = [32 for planet in planets]
print("Constant list comprehension:", constant_list)

# -----------------------------
# List comprehensions with functions
# -----------------------------
# count negative numbers in a list
def count_negatives(nums):
    """Return the number of negative numbers in the list"""
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative += 1
    return n_negative

print("Count negatives (for loop):", count_negatives([5, -1, -2, 0, 3]))

# using list comprehension
def count_negatives_lc(nums):
    return len([num for num in nums if num < 0])

print("Count negatives (list comprehension):", count_negatives_lc([5, -1, -2, 0, 3]))

# using sum of booleans (most compact)
def count_negatives_sum(nums):
    return sum([num < 0 for num in nums])

print("Count negatives (sum of booleans):", count_negatives_sum([5, -1, -2, 0, 3]))
