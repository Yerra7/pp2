"""
Python Tuples
"""
#-----------------------------------------------------
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#-----------------------------------------------------
thistuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple1)
#-----------------------------------------------------
thistuple2 = ("apple", "banana", "cherry")
print(len(thistuple2))
#-----------------------------------------------------
thistuple3 = ("apple",)
print(type(thistuple3))

#NOT a tuple
thistuple4 = ("apple")
print(type(thistuple4))
#-----------------------------------------------------
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
#-----------------------------------------------------
tuple4 = ("abc", 34, True, 40, "male")
#-----------------------------------------------------
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#-----------------------------------------------------
thistuple5 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple5)
#-----------------------------------------------------