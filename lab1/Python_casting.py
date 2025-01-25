# Python Casting
''' 
In Python, you can cast a variable to a specific type using constructor functions. 
Casting allows you to specify the type of a variable when necessary.

Common casting functions:
1. int() - Converts to an integer.
2. float() - Converts to a floating-point number.
3. str() - Converts to a string.
'''

# Example: Integers
''' 
int() can convert:
- an integer literal,
- a float literal (by removing decimals),
- or a string literal (if the string represents a whole number).
'''

x = int(1)   # x will be 1 (integer)
y = int(2.8) # y will be 2 (integer, decimals are discarded)
z = int("3") # z will be 3 (string "3" is converted to integer)

# Example: Floats
''' 
float() can convert:
- an integer literal,
- a float literal,
- or a string literal (if the string represents a float or integer).
'''

x = float(1)     # x will be 1.0 (converted to float)
y = float(2.8)   # y will be 2.8 (already a float)
z = float("3")   # z will be 3.0 (string "3" is converted to float)
w = float("4.2") # w will be 4.2 (string "4.2" is converted to float)

# Example: Strings
''' 
str() can convert:
- a string literal,
- an integer literal,
- or a float literal.
'''

x = str("s1")   # x will be 's1' (already a string)
y = str(2)      # y will be '2' (integer 2 is converted to string)
z = str(3.0)    # z will be '3.0' (float 3.0 is converted to string)
