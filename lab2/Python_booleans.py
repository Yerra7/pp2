# Python Booleans
"""
Booleans represent one of two values: True or False.
They are used in conditions and logical operations.
"""

# Boolean Values
print(10 > 9)   # True
print(10 == 9)  # False
print(10 < 9)   # False

# Using Booleans in an if-else statement
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")  # This will be printed

# Evaluating values with bool()
print(bool("Hello"))  # True
print(bool(15))       # True

# Evaluating variables
x = "Hello"
y = 15

print(bool(x))  # True
print(bool(y))  # True

# Most values are True
print(bool("abc"))  # True
print(bool(123))    # True
print(bool(["apple", "cherry", "banana"]))  # True

# Some values evaluate to False
print(bool(False))  # False
print(bool(None))   # False
print(bool(0))      # False
print(bool(""))     # False
print(bool(()))     # False
print(bool([]))     # False
print(bool({}))     # False

# Objects with __len__() returning 0 evaluate to False
class MyClass:
    def __len__(self):
        return 0

myobj = MyClass()
print(bool(myobj))  # False

# Functions that return Booleans
def myFunction():
    return True

print(myFunction())  # True

# Using Boolean return values in conditions
if myFunction():
    print("YES!")
else:
    print("NO!")

# Checking data types with isinstance()
x = 200
print(isinstance(x, int))  # True
