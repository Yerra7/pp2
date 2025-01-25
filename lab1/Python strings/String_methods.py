# String Methods
''' 
Python provides several built-in methods that can be used on strings.
Note: All string methods return new values and do not modify the original string.
'''

# Example: capitalize()
string = "hello"
new_string = string.capitalize()  # Converts the first character to upper case
print(new_string)  # Output: Hello

# Example: casefold()
string = "HELLO"
new_string = string.casefold()  # Converts string to lower case
print(new_string)  # Output: hello

# Example: count()
string = "hello world"
count = string.count("o")  # Returns the number of times 'o' appears in the string
print(count)  # Output: 2

# Example: endswith()
string = "hello"
ends_with = string.endswith("lo")  # Returns True if the string ends with 'lo'
print(ends_with)  # Output: True

# Example: find()
string = "hello world"
position = string.find("world")  # Returns the position where 'world' starts
print(position)  # Output: 6

# Example: format()
name = "John"
age = 25
formatted_string = "My name is {} and I am {} years old.".format(name, age)  # Formats the string
print(formatted_string)  # Output: My name is John and I am 25 years old.

# Example: isalnum()
string = "hello123"
is_alnum = string.isalnum()  # Returns True if all characters are alphanumeric
print(is_alnum)  # Output: True

# Example: isalpha()
string = "hello"
is_alpha = string.isalpha()  # Returns True if all characters are alphabetic
print(is_alpha)  # Output: True

# Example: isdecimal()
string = "12345"
is_decimal = string.isdecimal()  # Returns True if all characters are decimals
print(is_decimal)  # Output: True

# Example: islower()
string = "hello"
is_lower = string.islower()  # Returns True if all characters are lowercase
print(is_lower)  # Output: True

# Example: join()
list_of_strings = ["hello", "world"]
joined_string = " ".join(list_of_strings)  # Joins elements with a space
print(joined_string)  # Output: hello world

# Example: replace()
string = "hello world"
replaced_string = string.replace("world", "Python")  # Replaces 'world' with 'Python'
print(replaced_string)  # Output: hello Python

# Example: split()
string = "hello world"
split_string = string.split()  # Splits the string into a list at spaces
print(split_string)  # Output: ['hello', 'world']

# Example: upper()
string = "hello"
upper_string = string.upper()  # Converts the string to uppercase
print(upper_string)  # Output: HELLO

# Example: zfill()
string = "42"
filled_string = string.zfill(5)  # Pads the string with zeros at the beginning to length 5
print(filled_string)  # Output: 00042
