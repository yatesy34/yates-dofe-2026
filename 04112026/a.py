# 26/10/26 w3schools python: 
# dictionaries, if else, match, while loops, for loops
# end at for loops

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
thisdict.update({"year": 2020}) 
print(thisdict)
thisdict["newYear"] = 2018
print(thisdict)
thisdict.update({"newYear": 2020}) 
print(thisdict)
thisdict.pop('brand') # or del thisdict['brand']
print(thisdict)
thisdict.popitem() # last
print(thisdict)
# del thisdict
thisdict.clear()
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for i in thisdict:
  print(i)
  print(thisdict[i])
for i in thisdict.values():
  print(i)
for i in thisdict.keys():
  print(i)
for x, y in thisdict.items():
  print(x, y)

newdict = thisdict.copy()
newdict = dict(thisdict)
print(newdict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 
print(myfamily['child2']['name'])
for x, obj in myfamily.items():
  print(x)
  for y in obj:
    print(y , ":", obj[y])

# Create the dictionary
car = {"brand": "Ford", "model": "Mustang", "year": 2024}
# Print the model
print(car['model'])
# Add a color key
car['color'] = "red"
# Remove the brand key
car.pop('brand')
# Print the dictionary
print(car)

# ---------
#  if else
# ---------

is_logged_in = True
if is_logged_in:
  print("Welcome back!")
# Zero (0), empty strings (""), None, and empty collections are treated as False. Everything else is treated as True.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
a = 5
b = 2
if a > b: print("a is greater than b")
print(a) if a > b else print(b) # This is called a conditional expression (sometimes known as a "ternary operator").
a = 10
b = 20
bigger = a if a > b else b # variable = value_if_true if condition else value_if_false 
print(bigger)
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)
score = 85

if score > 90:
  pass # do nothing
print("Score processed")

# Create age variable
age = 20
# Write if/elif/else
if age < 13:
	print("Child")
elif age < 18:
	print("Teenager")
else:
	print("Adult")

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
    print("no matches")
    day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")

# Create variable day
day = 3
# Use match statement
match day:
	case 3:
		print("Wednesday")
	case _:
		print("Other day")

# -------------
#  while loops
# -------------

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# Create the i variable
i = 0
# While loop: print 1-5, skip 3 with continue
while i < 6:
	i += 1
	if i == 3:
		continue
	print(i)

# -----------
#  for loops
# -----------

for x in "banana":
  print(x)

# Create the fruits list
fruits = ["apple", "banana", "cherry"]
# Loop through fruits, break at "banana"
for i in fruits:
	print(i)
	if i == "banana": break
