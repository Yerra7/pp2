# Output Variables
''' 
The Python print() function is often used to output variables.
'''

# Example 1: Output a single variable
x = "Python is awesome"
print(x)  # Output: Python is awesome

# Example 2: Output multiple variables using a comma
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)  # Output: Python is awesome

# Example 3: Output multiple variables using the + operator
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)  # Output: Python is awesome
# Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

# Example 4: Using + for numerical values
x = 5
y = 10
print(x + y)  # Output: 15 (sum of x and y)

# Example 5: Combining string and number with + (this will cause an error)
# x = 5
# y = "John"
# print(x + y)  # Error: cannot concatenate string and int

# The best way to output multiple variables in print() function is by separating them with commas,
# which even support different data types.
x = 5
y = "John"
print(x, y)  # Output: 5 John
