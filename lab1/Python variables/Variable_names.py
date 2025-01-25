# Python - Variable Names
''' 
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:
- A variable name must start with a letter or the underscore character.
- A variable name cannot start with a number.
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _).
- Variable names are case-sensitive (age, Age, and AGE are three different variables).
- A variable name cannot be any of the Python keywords.
'''

# Legal variable names:
myvar = "John"          # Valid
my_var = "John"         # Valid
_my_var = "John"        # Valid
myVar = "John"          # Valid
MYVAR = "John"          # Valid
myvar2 = "John"         # Valid

# Illegal variable names:
# 2myvar = "John"       # Invalid, cannot start with a number
# my-var = "John"       # Invalid, cannot use hyphen
# my var = "John"       # Invalid, cannot have spaces

# Multi Words Variable Names
'''
Variable names with more than one word can be difficult to read.
There are several techniques to make them more readable:
'''

# Camel Case
myVariableName = "John"  # First word lowercase, subsequent words capitalized

# Pascal Case
MyVariableName = "John"  # Each word starts with a capital letter

# Snake Case
my_variable_name = "John"  # Each word separated by underscores
