# Python - Modify Strings
'''
Python provides a set of built-in methods that can be used to manipulate strings.
'''

# Upper Case
''' 
The upper() method returns the string in upper case.
'''

# Example:
a = "Hello, World!"
print(a.upper())  # Output: "HELLO, WORLD!"

# Lower Case
''' 
The lower() method returns the string in lower case.
'''

# Example:
a = "Hello, World!"
print(a.lower())  # Output: "hello, world!"

# Remove Whitespace
''' 
Whitespace refers to the space before and/or after the actual text. 
The strip() method removes any whitespace from the beginning or the end of the string.
'''

# Example:
a = " Hello, World! "
print(a.strip())  # Output: "Hello, World!"

# Replace String
''' 
The replace() method replaces a specified substring with another substring.
'''

# Example:
a = "Hello, World!"
print(a.replace("H", "J"))  # Output: "Jello, World!"

# Split String
''' 
The split() method splits the string into a list based on the specified separator. 
In this example, the separator is a comma.
'''

# Example:
a = "Hello, World!"
print(a.split(","))  # Output: ['Hello', ' World!']

# Note: You can learn more about Lists in the Python Lists chapter.
