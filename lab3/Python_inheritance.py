"""
Python Inheritance
"""
"""
#-----------------------------------------------------
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
#-----------------------------------------------------
class Student(Person):
  pass
#-----------------------------------------------------
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
#-----------------------------------------------------
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
#-----------------------------------------------------
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
#-----------------------------------------------------
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
#-----------------------------------------------------
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
#-----------------------------------------------------
"""

print("-----------------------------------------------------")
class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def printname(self):
		print(self.firstname, self.lastname)

print("Example 1: Person Class")
x = Person("John", "Doe")
x.printname()

print("-----------------------------------------------------")
print("Example 2: Student Class (inherits Person without modification)")
class Student(Person):
	pass

s1 = Student("Alice", "Smith")
s1.printname()

print("-----------------------------------------------------")
print("Example 3: Student Class with explicit Person.__init__() call")
class Student(Person):
	def __init__(self, fname, lname):
		Person.__init__(self, fname, lname)

s2 = Student("Bob", "Brown")
s2.printname()

print("-----------------------------------------------------")
print("Example 4: Student Class using super()")
class Student(Person):
	def __init__(self, fname, lname):
		super().__init__(fname, lname)

s3 = Student("Charlie", "Davis")
s3.printname()

print("-----------------------------------------------------")
print("Example 5: Student Class with a graduation year attribute")
class Student(Person):
	def __init__(self, fname, lname):
		super().__init__(fname, lname)
		self.graduationyear = 2019

s4 = Student("David", "Evans")
s4.printname()
print("Graduation Year:", s4.graduationyear)

print("-----------------------------------------------------")
print("Example 6: Student Class with customizable graduation year")
class Student(Person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname)
		self.graduationyear = year

s5 = Student("Mike", "Olsen", 2019)
s5.printname()
print("Graduation Year:", s5.graduationyear)

print("-----------------------------------------------------")
print("Example 7: Student Class with welcome method")
class Student(Person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname)
		self.graduationyear = year

	def welcome(self):
		print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

s6 = Student("Sarah", "Williams", 2023)
s6.printname()
s6.welcome()

print("-----------------------------------------------------")