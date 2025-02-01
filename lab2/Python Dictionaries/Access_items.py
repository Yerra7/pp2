"""
Python - Access Dictionary Items
"""
#-----------------------------------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
#-----------------------------------------------------
x = thisdict.get("model")
#-----------------------------------------------------
x = thisdict.keys()
#-----------------------------------------------------
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x1 = car.keys()

print(x1) #before the change

car["color"] = "white"

print(x1) #after the change
#-----------------------------------------------------
x1 = thisdict.values()
#-----------------------------------------------------
car1 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x2 = car1.values()

print(x2) #before the change

car1["year"] = 2020

print(x2) #after the change
#-----------------------------------------------------
car2 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x3 = car2.values()

print(x3) #before the change

car2["color"] = "red"

print(x3) #after the change
#-----------------------------------------------------
x3 = thisdict.items()
#-----------------------------------------------------
car4 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x4 = car4.items()

print(x4) #before the change

car4["year"] = 2020

print(x4) #after the change
#-----------------------------------------------------
car5 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x5 = car5.items()

print(x5) #before the change

car5["color"] = "red"

print(x5) #after the change
#-----------------------------------------------------
thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict1:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
#-----------------------------------------------------