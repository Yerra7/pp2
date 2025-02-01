# Python Operators

# Arithmetic Operators
print("Arithmetic Operators:")
a, b = 10, 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b)  # Exponentiation
print(a // b)  # Floor Division

print("\nAssignment Operators:")
x = 5
x += 3
print(x)  # Same as x = x + 3

x -= 2
print(x)  # Same as x = x - 2

x *= 2
print(x)  # Same as x = x * 2

x /= 3
print(x)  # Same as x = x / 3

x %= 3
print(x)  # Modulus assignment

x //= 2
print(x)  # Floor division assignment

x **= 2
print(x)  # Exponentiation assignment

# Comparison Operators
print("\nComparison Operators:")
print(a == b)  # Equal
print(a != b)  # Not equal
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to

# Logical Operators
print("\nLogical Operators:")
print(a > 5 and b < 10)  # True
print(a > 5 or b > 10)   # True
print(not(a > 5))        # False

# Identity Operators
print("\nIdentity Operators:")
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)       # True (same object)
print(x is not z)   # True (different objects)

# Membership Operators
print("\nMembership Operators:")
print(2 in x)       # True
print(5 not in x)   # True

# Bitwise Operators
print("\nBitwise Operators:")
p, q = 6, 3  # 6 = 110, 3 = 011 in binary
print(p & q)  # AND  -> 2 (010)
print(p | q)  # OR   -> 7 (111)
print(p ^ q)  # XOR  -> 5 (101)
print(~p)     # NOT  -> -7 (two's complement)
print(p << 1) # Left shift -> 12 (1100)
print(q >> 1) # Right shift -> 1 (001)

# Operator Precedence
print("\nOperator Precedence:")
print((6 + 3) - (6 + 3))  # Parentheses first
print(100 + 5 * 3)        # Multiplication before addition
print(5 + 4 - 7 + 3)      # Left to right evaluation

