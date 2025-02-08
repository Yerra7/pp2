"""
Python Lambda
"""
"""
#-----------------------------------------------------
x = lambda a : a + 10
print(x(5))
#-----------------------------------------------------
x1 = lambda a, b : a * b
print(x1(5, 6))
#-----------------------------------------------------
x2 = lambda a, b, c : a + b + c
print(x2(5, 6, 2))
#-----------------------------------------------------
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
#-----------------------------------------------------
def myfunc1(n):
  return lambda a : a * n

mytripler = myfunc1(3)

print(mytripler(11))
#-----------------------------------------------------
def myfunc2(n):
  return lambda a : a * n

mydoubler1 = myfunc2(2)
mytripler1 = myfunc2(3)

print(mydoubler1(11))
print(mytripler1(11))
#-----------------------------------------------------
"""

print("----------------------------------------------------------------------------------------")
print('Python Lambda')

print("----------------------------------------------------------------------------------------")
print('Example 1: Simple Lambda Function')

x = lambda a: a + 10
print('x = lambda a: a + 10')
print('print(x(5))')
print(x(5))

print("----------------------------------------------------------------------------------------")
print('Example 2: Lambda with Two Arguments')

x1 = lambda a, b: a * b
print('x1 = lambda a, b: a * b')
print('print(x1(5, 6))')
print(x1(5, 6))

print("----------------------------------------------------------------------------------------")
print('Example 3: Lambda with Three Arguments')

x2 = lambda a, b, c: a + b + c
print('x2 = lambda a, b, c: a + b + c')
print('print(x2(5, 6, 2))')
print(x2(5, 6, 2))

print("----------------------------------------------------------------------------------------")
print('Example 4: Using Lambda in a Function')

def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
print('def myfunc(n): return lambda a: a * n')
print('mydoubler = myfunc(2)')
print('print(mydoubler(11))')
print(mydoubler(11))

print("----------------------------------------------------------------------------------------")
print('Example 5: Tripling with Lambda')

def myfunc1(n):
    return lambda a: a * n

mytripler = myfunc1(3)
print('def myfunc1(n): return lambda a: a * n')
print('mytripler = myfunc1(3)')
print('print(mytripler(11))')
print(mytripler(11))

print("----------------------------------------------------------------------------------------")
print('Example 6: Doubling and Tripling Using Lambda')

def myfunc2(n):
    return lambda a: a * n

mydoubler1 = myfunc2(2)
mytripler1 = myfunc2(3)
print('def myfunc2(n): return lambda a: a * n')
print('mydoubler1 = myfunc2(2)')
print('mytripler1 = myfunc2(3)')
print('print(mydoubler1(11))')
print('print(mytripler1(11))')
print(mydoubler1(11))
print(mytripler1(11))

print("----------------------------------------------------------------------------------------")