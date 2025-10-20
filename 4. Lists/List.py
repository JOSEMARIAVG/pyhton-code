"""
Python Lists and Tuples
This script covers:
- Lists: ordered, mutable sequences
- Indexing and slicing
- List functions and methods
- Searching lists
- Tuples: immutable sequences
"""

# -----------------------------
# Creating lists
# -----------------------------
primes = [2, 3, 5, 7]  # List of integers
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']  # List of strings

# List of lists
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

# Mixed types in a list
my_favourite_things = [32, 'raindrops on roses', help]

# -----------------------------
# Indexing
# -----------------------------
print(planets[0])   # 'Mercury', first element (index 0)
print(planets[1])   # 'Venus'
print(planets[-1])  # 'Neptune', last element
print(planets[-2])  # 'Uranus', second last element

# -----------------------------
# Slicing
# -----------------------------
print(planets[0:3])  # ['Mercury', 'Venus', 'Earth']
print(planets[:3])   # same as above
print(planets[3:])   # from index 3 to end
print(planets[1:-1]) # all except first and last
print(planets[-3:])  # last 3 planets

# -----------------------------
# Modifying lists (mutable)
# -----------------------------
planets[3] = 'Malacandra'  # rename Mars
print(planets)

# Modify first 3 elements
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)

# Restore original names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars']
print(planets)

# -----------------------------
# List functions
# -----------------------------
print(len(planets))       # length of list
print(sorted(planets))    # alphabetical order

primes = [2, 3, 5, 7]
print(sum(primes))        # sum of list
print(max(primes))        # maximum

# -----------------------------
# Objects, attributes and methods
# -----------------------------
x = 12
print(x.imag)             # imaginary part of a number
c = 12 + 3j
print(c.imag)             # 3.0

print(x.bit_length())     # number of bits to represent x

help(x.bit_length)        # documentation

# -----------------------------
# List methods
# -----------------------------
planets.append('Pluto')   # add element to end
print(planets)

last_planet = planets.pop()  # remove last element and return it
print(last_planet)
print(planets)

print(planets.index('Earth'))  # find index of element

# Check existence with 'in'
print('Earth' in planets)        # True
print('Calbefraques' in planets) # False

help(planets)  # see all list methods

# -----------------------------
# Tuples
# -----------------------------
t = (1, 2, 3)    # tuple with parentheses
t2 = 1, 2, 3     # equivalent

# Tuples are immutable
try:
    t[0] = 100
except TypeError as e:
    print(e)

# Tuples as multiple return values
x = 0.125
numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)  # 0.125

# Swapping variables using tuple unpacking
a = 1
b = 0
a, b = b, a
print(a, b)  # 0 1
