class MyClass:
  x = 5
print(MyClass)
# <class '__main__.MyClass'>

class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)
# 5

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
# John
# 36

# Note: The __init__() function is called automatically every time the class is being used to create a new object.

# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)
# <__main__.Person object at 0x15039e602100>

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"    

p1 = Person("John", 36)

print(p1)
# John(36)

# Objects can also contain methods. Methods in objects are functions that belong to the object.
# Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
# Hello my name is John

# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:

# Use the words mysillyobject and abc instead of self:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
# Hello my name is John

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)
# 40

# You can delete properties on objects by using the del keyword:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1.age
print(p1.age)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1
print(p1)


# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class Person:
  pass
# having an empty class definition like this, would raise an error without the pass statement



















