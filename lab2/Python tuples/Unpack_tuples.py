"""
Python - Unpack Tuples
"""
#-----------------------------------------------------
fruits = ("apple", "banana", "cherry")
#-----------------------------------------------------
fruits1 = ("apple", "banana", "cherry")

(green, yellow, red) = fruits1

print(green)
print(yellow)
print(red)
#-----------------------------------------------------
fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits2

print(green)
print(yellow)
print(red)
#-----------------------------------------------------
fruits3 = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits3

print(green)
print(tropic)
print(red)
#-----------------------------------------------------