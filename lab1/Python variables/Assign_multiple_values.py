# Python - Assign Multiple Values

'''
Python allows you to assign values to multiple variables in one line.
'''

# Example 1: Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"  # Assigning different values to x, y, z
print(x)  # Output: Orange
print(y)  # Output: Banana
print(z)  # Output: Cherry

# Note: The number of variables must match the number of values.

# Example 2: One Value to Multiple Variables
x = y = z = "Orange"  # Assigning the same value to x, y, and z
print(x)  # Output: Orange
print(y)  # Output: Orange
print(z)  # Output: Orange

# Unpack a Collection
'''
Python allows you to unpack a collection like a list or tuple into variables.
'''

# Example 3: Unpack a List
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits  # Unpacking the values of the list into variables x, y, z
print(x)  # Output: apple
print(y)  # Output: banana
print(z)  # Output: cherry
