# String Format
''' 
In Python, we cannot directly combine strings and numbers like this:
'''

# Example of incorrect way:
age = 36
# txt = "My name is John, I am " + age  # This will raise an error

# But we can combine strings and numbers using f-strings or the format() method!

# F-Strings
''' 
F-Strings were introduced in Python 3.6 and are now the preferred way of formatting strings.
To create an f-string, simply put an "f" before the string literal, and add curly brackets {} as placeholders for variables or expressions.
'''

# Example using f-string:
age = 36
txt = f"My name is John, I am {age}"
print(txt)  # Output: My name is John, I am 36

# Placeholders and Modifiers
''' 
A placeholder in an f-string can contain variables, operations, functions, and modifiers to format the value.
'''

# Example with a variable in a placeholder:
price = 59
txt = f"The price is {price} dollars"
print(txt)  # Output: The price is 59 dollars

# Example with a modifier in the placeholder:
''' 
Modifiers allow you to control how the value is displayed. For instance, .2f formats a number to 2 decimal places.
'''

# Display price with 2 decimals:
txt = f"The price is {price:.2f} dollars"
print(txt)  # Output: The price is 59.00 dollars

# A placeholder can also contain Python code, such as math operations:
txt = f"The price is {20 * 59} dollars"
print(txt)  # Output: The price is 1180 dollars
