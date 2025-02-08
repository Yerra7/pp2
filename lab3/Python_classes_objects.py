"""
Python Classes and Objects
"""
"""#-----------------------------------------------------
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)
#-----------------------------------------------------
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
#-----------------------------------------------------
class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p12 = Person1("John", 36)

print(p12)
#-----------------------------------------------------
class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p13 = Person2("John", 36)

print(p13)
#-----------------------------------------------------
class Person3:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc1(self):
    print("Hello my name is " + self.name)

p14 = Person3("John", 36)
p14.myfunc1()
#-----------------------------------------------------
class Person4:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc2(abc):
    print("Hello my name is " + abc.name)

p15 = Person4("John", 36)  # Используем правильный класс
p15.myfunc2()  # Теперь код работает без ошибки
#-----------------------------------------------------"""

while True:
	print("-----------------------------------------------------")
	print("Enter number of wanted Example to have been compiled 1-6: ")
	choice = input()

	if choice == "0":
		break

	elif choice == "1":
		print("-----------------------------------------------------")
		class MyClass:
			x = 5
		p1 = MyClass()
		print(p1.x)

	elif choice == "2":
		print("-----------------------------------------------------")
		class Person:
			def __init__(self, name, age):
				self.name = name
				self.age = age
		p1 = Person("John", 36)
		print(p1.name)
		print(p1.age)

	elif choice == "3":
		print("-----------------------------------------------------")
		class Person1:
			def __init__(self, name, age):
				self.name = name
				self.age = age
		p12 = Person1("John", 36)
		print(p12)

	elif choice == "4":
		print("-----------------------------------------------------")
		class Person2:
			def __init__(self, name, age):
				self.name = name
				self.age = age
			def __str__(self):
				return f"{self.name}({self.age})"
		p13 = Person2("John", 36)
		print(p13)

	elif choice == "5":
		print("-----------------------------------------------------")
		class Person3:
			def __init__(self, name, age):
				self.name = name
				self.age = age
			def myfunc1(self):
				print("Hello my name is " + self.name)
		p14 = Person3("John", 36)
		p14.myfunc1()

	elif choice == "6":
		print("-----------------------------------------------------")
		class Person4:
			def __init__(mysillyobject, name, age):
				mysillyobject.name = name
				mysillyobject.age = age
			def myfunc2(abc):
				print("Hello my name is " + abc.name)
		p15 = Person4("John", 36)
		p15.myfunc2()

	else:
		print("Invalid input.")