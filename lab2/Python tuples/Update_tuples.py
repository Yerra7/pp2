"""
Python - Update Tuples
"""
#-----------------------------------------------------
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#-----------------------------------------------------
thistuple = ("apple", "banana", "cherry")
y1 = list(thistuple)
y1.append("orange")
thistuple = tuple(y1)
#-----------------------------------------------------
thistuple1 = ("apple", "banana", "cherry")
y2 = ("orange",)
thistuple1 += y2

print(thistuple1)
#-----------------------------------------------------
thistuple2 = ("apple", "banana", "cherry")
y3 = list(thistuple2)
y3.remove("apple")
thistuple2 = tuple(y3)
#-----------------------------------------------------
thistuple3 = ("apple", "banana", "cherry")
del thistuple3
print(thistuple3) #this will raise an error because the tuple no longer exists
#-----------------------------------------------------