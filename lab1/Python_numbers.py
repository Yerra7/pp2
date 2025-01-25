# Python Numbers
''' 
There are three numeric types in Python:
1. int
2. float
3. complex

Variables of numeric types are created when you assign a value to them.
'''

# Example
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# To verify the type of any object, use the type() function
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'complex'>

# Int
''' 
Int (integer) is a whole number, positive or negative, without decimals, and of unlimited length.
'''

# Example of integers:
x = 1
y = 35656222554887711
z = -3255522

print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'int'>
print(type(z))  # Output: <class 'int'>

# Float
''' 
Float (floating point number) is a number, positive or negative, containing one or more decimals.
'''

# Example of floats:
x = 1.10
y = 1.0
z = -35.59

print(type(x))  # Output: <class 'float'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'float'>

# Float can also represent scientific numbers with an "e" to indicate the power of 10:
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))  # Output: <class 'float'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'float'>

# Complex
''' 
Complex numbers are written with a "j" as the imaginary part.
'''

# Example of complex numbers:
x = 3 + 5j
y = 5j
z = -5j

print(type(x))  # Output: <class 'complex'>
print(type(y))  # Output: <class 'complex'>
print(type(z))  # Output: <class 'complex'>

# Type Conversion
''' 
You can convert from one type to another using int(), float(), and complex() methods.
'''

# Example of type conversion:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# Convert from int to float:
a = float(x)

# Convert from float to int:
b = int(y)

# Convert from int to complex:
c = complex(x)

print(a)  # Output: 1.0
print(b)  # Output: 2
print(c)  # Output: (1+0j)

print(type(a))  # Output: <class 'float'>
print(type(b))  # Output: <class 'int'>
print(type(c))  # Output: <class 'complex'>

# Note: Complex numbers cannot be converted into other number types.

# Random Number
''' 
Python does not have a random() function built-in to make random numbers. 
However, Python has a built-in module called random that can be used to generate random numbers.
'''

# Example using the random module:
import random

print(random.randrange(1, 10))  # Output: A random number between 1 and 9
