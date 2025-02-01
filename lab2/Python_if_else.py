"""
Python If ... Else
"""
#-----------------------------------------------------
a = 33
b = 200
if b > a:
  print("b is greater than a")
#-----------------------------------------------------
a1 = 33
b1 = 33
if b1 > a1:
  print("b is greater than a")
elif a1 == b1:
  print("a and b are equal")
#-----------------------------------------------------
a2 = 200
b2 = 33
if b2 > a2:
  print("b is greater than a")
elif a2 == b2:
  print("a and b are equal")
else:
  print("a is greater than b")
#-----------------------------------------------------
a3 = 200
b3 = 33
if b3 > a3:
  print("b is greater than a")
else:
  print("b is not greater than a")
#-----------------------------------------------------
if a3 > b3: print("a is greater than b")
#-----------------------------------------------------
a4 = 2
b4 = 330
print("A") if a4 > b4 else print("B")
#-----------------------------------------------------
a5 = 330
b5 = 330
print("A") if a5 > b5 else print("=") if a5 == b5 else print("B")
#-----------------------------------------------------
a6 = 200
b6 = 33
c6 = 500
if a6 > b6 and c6 > a6:
  print("Both conditions are True")
#-----------------------------------------------------
a7 = 200
b7 = 33
c7 = 500
if a7 > b7 or a7 > c7:
  print("At least one of the conditions is True")
#-----------------------------------------------------
a8 = 33
b8 = 200
if not a8 > b8:
  print("a is NOT greater than b")
#-----------------------------------------------------
xq = 41

if xq > 10:
  print("Above ten,")
  if xq > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#-----------------------------------------------------
aa = 33
ba = 200

if ba > aa:
  pass
#-----------------------------------------------------