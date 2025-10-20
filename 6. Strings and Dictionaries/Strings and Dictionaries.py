"""
Python Strings and Dictionaries
Covers:
- String syntax and manipulation
- String methods
- Formatting with str.format()
- Dictionaries and dictionary comprehensions
"""

# -----------------------------
# Strings
# -----------------------------
x = 'Pluto is a planet'
y = "Pluto is a planet"
print("Are x and y equal?", x == y)

# Quotes inside strings
print("Pluto's a planet!")
print('My dog is named "Pluto"')

# Escaping characters
print('Pluto\'s a planet!')

# Newlines
hello = "hello\nworld"
print(hello)

triplequoted_hello = """hello
world"""
print(triplequoted_hello)
print("Are they equal?", triplequoted_hello == hello)

# Strings are sequences
planet = 'Pluto'
print("First character:", planet[0])
print("Last three characters:", planet[-3:])
print("Length:", len(planet))
print("Loop over string with comprehension:", [char+'!' for char in planet])

# Strings are immutable
try:
    planet[0] = 'B'
except TypeError as e:
    print("Error:", e)

# String methods
claim = "Pluto is a planet!"
print("Uppercase:", claim.upper())
print("Lowercase:", claim.lower())
print("Index of 'plan':", claim.index('plan'))
print("Starts with 'Pluto'? ", claim.startswith('Pluto'))
print("Ends with 'planet'? ", claim.endswith('planet'))

# Split and join
words = claim.split()
print("Split words:", words)

datestr = '1956-01-31'
year, month, day = datestr.split('-')
print("Reformatted date:", '/'.join([month, day, year]))

# Joining with transformations
print(' 👏 '.join([word.upper() for word in words]))

# String formatting
position = 9
print("{}, you'll always be the {}th planet to me.".format(planet, position))

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390

formatted_str = "{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population
)
print(formatted_str)

# Using positional indices in format
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

# -----------------------------
# Dictionaries
# -----------------------------
numbers = {'one':1, 'two':2, 'three':3}
print("Value for 'one':", numbers['one'])

# Adding/changing keys
numbers['eleven'] = 11
numbers['one'] = 'Pluto'
print("Updated numbers dictionary:", numbers)

# Dictionary comprehension
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print("Planet to initial mapping:", planet_to_initial)

# Check if key exists
print("'Saturn' in dict?", 'Saturn' in planet_to_initial)
print("'Betelgeuse' in dict?", 'Betelgeuse' in planet_to_initial)

# Looping over keys
for k in numbers:
    print("{} = {}".format(k, numbers[k]))

# Access keys and values
print("Sorted initials:", ' '.join(sorted(planet_to_initial.values())))

# Looping over items
for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))

# Full help on dictionaries
# help(dict)
