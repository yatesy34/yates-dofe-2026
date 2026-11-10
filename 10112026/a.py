# 10/11/26 w3schools python: 
# functions
# end at lambda functions

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") 

# Create the fruits list
fruits = ["apple", "banana", "cherry"]
# Loop through fruits, break at "banana"
for fruit in fruits:
	if fruit == "banana": break	
	print(fruit)

# -----------
#  functions
# -----------

def my_function():
  print("Hello from a function")

my_function()

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50)) 

def get_greeting():
  print("Hello from a function")

print(get_greeting())

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument 

def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus") 

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5) #However, positional arguments must come before keyword arguments:

def my_function(name, /):
  print("Hello", name)

my_function("Emil") 

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result) 
#*args (arbitrary arguments) and **kwargs allow functions to accept a unknown number of arguments.
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus") 

def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1)) 

def my_function(**kid):
  print("His last name is " + kid["lname"])
  print(type(kid))

my_function(fname = "Tobias", lname = "Refsnes") 

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen") 
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args) # tuple 
  print("Keyword arguments:", kwargs) # dict

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo") 

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result) 

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes") 

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc() 
#A variable created outside of a function is global and can be used by anyone

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x) 

def myfunc():
  global x # variable belongs to the global scope
  x = 300

myfunc()

print(x) 

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1()) 

# Python follows the LEGB rule when looking up variable names, and searches for them in this order:

#    Local - Inside the current function
#    Enclosing - Inside enclosing functions (from inner to outer)
#    Global - At the top level of the module
#    Built-in - In Python's built-in namespace

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())

def myfunction():
  return "Have a great day!"

print(myfunction._name_) 

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction._name_) # loses it

import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction._name_)

# lambda arguments : expression
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a : a + 10
print(x(5))
x = lambda a, b : a * b
print(x(5,6))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x : x * 2, numbers))
print(doubled)
numbers = [1,2 ,3 ,4 ,5 ,6 ,7 , 8]
odd_numbers = list(filter(lambda x : x % 2 != 0, numbers))
print(odd_numbers)

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key = lambda x : x[1])
print(sorted_students)
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)