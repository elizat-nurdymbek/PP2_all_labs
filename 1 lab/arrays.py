# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

# Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.

cars = ["Ford", "Volvo", "BMW"]
print(cars)
# ['Ford', 'Volvo', 'BMW']

# You refer to an array element by referring to the index number.
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)
# Ford

cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)
# ['Toyota', 'Volvo', 'BMW']

cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)
# 3

# Note: The length of an array is always one more than the highest array index.

cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)
# Ford
# Volvo
# BMW

# You can use the append() method to add an element to an array.
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)
# ['Ford', 'Volvo', 'BMW', 'Honda']

# You can use the pop() method to remove an element from the array.
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)
# ['Ford', 'BMW']

# You can also use the remove() method to remove an element from the array.
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)
# ['Ford', 'BMW']

# Note: The list's remove() method only removes the first occurrence of the specified value.

# append()	  Adds an element at the end of the list
# clear()	  Removes all the elements from the list
# copy()	  Returns a copy of the list
# count()	  Returns the number of elements with the specified value
# extend()	  Add the elements of a list (or any iterable), to the end of the current list
# index()	  Returns the index of the first element with the specified value
# insert()	  Adds an element at the specified position
# pop()	      Removes the element at the specified position
# remove()	  Removes the first item with the specified value
# reverse()	  Reverses the order of the list
# sort()	  Sorts the list



