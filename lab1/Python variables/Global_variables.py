# Global Variables
''' 
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
'''

# Example: Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
    print("Python is " + x)  # Accessing global variable inside the function

myfunc()

# Example: Create a variable inside a function, with the same name as the global variable
x = "awesome"  # Global variable

def myfunc():
    x = "fantastic"  # Local variable, shadows the global variable
    print("Python is " + x)  # Accessing local variable inside the function

myfunc()

# The global variable 'x' remains unchanged outside the function
print("Python is " + x)  # Output: Python is awesome


# The global Keyword
''' 
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
'''

# Example: Using the global keyword to create a global variable inside a function
def myfunc():
    global x  # Declare 'x' as a global variable
    x = "fantastic"  # Modifying the global variable

myfunc()

print("Python is " + x)  # Output: Python is fantastic


# Example: Changing the value of a global variable inside a function using the global keyword
x = "awesome"  # Initial global variable

def myfunc():
    global x  # Referring to the global variable
    x = "fantastic"  # Changing the value of the global variable

myfunc()

print("Python is " + x)  # Output: Python is fantastic
