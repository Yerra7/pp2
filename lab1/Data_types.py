# Python - Data Types
''' 
In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
'''

# Built-in Data Types
'''
Python has the following data types built-in by default, in these categories:
- Text Type: str
- Numeric Types: int, float, complex
- Sequence Types: list, tuple, range
- Mapping Type: dict
- Set Types: set, frozenset
- Boolean Type: bool
- Binary Types: bytes, bytearray, memoryview
- None Type: NoneType
'''

# Getting the Data Type
'''
You can get the data type of any object by using the type() function:
'''

x = 5  # x is of type int
print(type(x))  # Output: <class 'int'>

# Setting the Data Type
'''
In Python, the data type is set when you assign a value to a variable.
'''

x = "Hello World"  # x is of type str
x = 20             # x is of type int
x = 20.5           # x is of type float
x = 1j             # x is of type complex
x = ["apple", "banana", "cherry"]  # x is of type list
x = ("apple", "banana", "cherry")  # x is of type tuple
x = range(6)       # x is of type range
x = {"name": "John", "age": 36}    # x is of type dict
x = {"apple", "banana", "cherry"}  # x is of type set
x = frozenset({"apple", "banana", "cherry"})  # x is of type frozenset
x = True            # x is of type bool
x = b"Hello"        # x is of type bytes
x = bytearray(5)    # x is of type bytearray
x = memoryview(bytes(5))  # x is of type memoryview
x = None            # x is of type NoneType

# Setting the Specific Data Type
'''
If you want to specify the data type, you can use the following constructor functions:
'''

x = str("Hello World")   # x is of type str
x = int(20)              # x is of type int
x = float(20.5)          # x is of type float
x = complex(1j)          # x is of type complex
x = list(("apple", "banana", "cherry"))  # x is of type list
x = tuple(("apple", "banana", "cherry"))  # x is of type tuple
x = range(6)             # x is of type range
x = dict(name="John", age=36)  # x is of type dict
x = set(("apple", "banana", "cherry"))  # x is of type set
x = frozenset(("apple", "banana", "cherry"))  # x is of type frozenset
x = bool(5)              # x is of type bool
x = bytes(5)             # x is of type bytes
x = bytearray(5)         # x is of type bytearray
x = memoryview(bytes(5))  # x is of type memoryview
