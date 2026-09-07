"""
I added a docstring here to explain that this script is used for greeting and doing basic math.
"""

def greet(name):
    print(f"Hello, {name}!")

greet("World")

a = 5
b = 100

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

add_result = add(a, b)
subtract_result = subtract(a, b)

print(add_result)
print(subtract_result)
