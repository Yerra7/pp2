# Python Variables
''' 
Variables are used to store data values in Python.
In Python, a variable is created the moment you first assign a value to it. 
You don't need to declare a variable type explicitly.
'''

x = 5  # x is an integer
y = "John"  # y is a string

print(x)  # Output: 5
print(y)  # Output: John

''' 
Variables can change their type after being set, which is unique to Python.
Here, x initially holds an integer value, but then it's reassigned to a string.
'''

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)    # Output: Sally

''' 
Casting: If you want to specify the data type of a variable, you can use casting functions.
Casting will convert the value into the type of your choice.
'''

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Get the Type
''' 
You can check the type of a variable using the type() function. 
This will return the data type of the value stored in the variable.
'''

print(type(x))  # Output: <class 'str'>
print(type(y))  # Output: <class 'int'>

''' 
Single or Double Quotes: String variables can be defined using either single or double quotes.
'''

x = "John"  # This is fine
x = 'John'  # This is also fine

''' 
Variable names are case-sensitive in Python, which means a and A are different variables.
'''

a = 4
A = "Sally"
# Here, 'a' and 'A' are two different variables.
