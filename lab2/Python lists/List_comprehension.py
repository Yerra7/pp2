# List Comprehension Example
# Without List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)  # Output: ['apple', 'banana', 'mango']

# With List Comprehension (One-liner)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)  # Output: ['apple', 'banana', 'mango']

# Conditional Examples:
# Only Accept Items Not Equal to "apple":
newlist = [x for x in fruits if x != "apple"]
print(newlist)  # Output: ['banana', 'cherry', 'kiwi', 'mango']

# Without the Condition (All Items):
newlist = [x for x in fruits]
print(newlist)  # Output: ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# Using `range()` to Create an Iterable:
newlist = [x for x in range(10)]
print(newlist)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Manipulating the Expression: Set the Values in Upper Case:
newlist = [x.upper() for x in fruits]
print(newlist)  # Output: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

# Set All Values to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)  # Output: ['hello', 'hello', 'hello', 'hello', 'hello']

# Conditional Expression: Return "orange" Instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)  # Output: ['apple', 'orange', 'cherry', 'kiwi', 'mango']
