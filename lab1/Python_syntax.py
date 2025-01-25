# Execute Python Syntax

# Python syntax can be executed in two main ways:
# 1. Directly in the Command Line:
# Example:
print("Example 1: Execute Python Syntax")
print("Hello, World!")  # This will output: Hello, World!

# 2. By creating a Python file (.py) and running it:
# Example: Save the following code as myfile.py and run it in the command line:
# python myfile.py
print("Example 2: Execute Python Syntax from a File")
print("This is executed from a Python file.")

# -------------------------------------------------

# Python Indentation

# Indentation in Python is crucial as it defines the structure of the code.
# Unlike other languages, Python uses indentation to define code blocks. 
# The indentation typically consists of spaces or tabs.

# Correct Indentation:
print("\nExample 3: Python Indentation (Correct)")
if 5 > 2:
    print("Five is greater than two!")

# Incorrect Indentation (This will cause an IndentationError):
''''
print("\nExample 4: Python Indentation (Incorrect)")
try:
    if 5 > 2:
    print("Five is greater than two!")  # This line will cause an error due to lack of indentation
except IndentationError as e:
    print(f"Error: {e}")
    '''

# -------------------------------------------------

# Python Variables

# In Python, you don't need to declare the type of a variable.
# You simply assign a value to a variable, and Python automatically determines the type.

x = 5
name = "Alice"
print("\nExample 5: Python Variables")
print(f"x = {x}, name = {name}")

# Python is dynamically typed, meaning no need to specify variable type:
# Example of an integer variable
integer_var = 10
# Example of a string variable
string_var = "Hello, World!"
print(f"integer_var = {integer_var}, string_var = {string_var}")

# -------------------------------------------------

# Comments in Python

# Comments are used to document the code and explain what specific parts of the code do.
# They are ignored by the Python interpreter and do not affect the program's execution.

# Single-line comment:
print("\nExample 6: Comments (Single-line)")
# This is a single-line comment. It does not affect the code.
print("This code will run despite the comment above.")

# Inline comment:
print("\nExample 7: Comments (Inline)")
print("Hello!")  # This comment explains the code, but it does not affect the output

# Multi-line comments using triple quotes:
print("\nExample 8: Comments (Multi-line)")
'''
This is a multi-line comment.
It can span multiple lines.
'''
print("This is after a multi-line comment block.")

# -------------------------------------------------
