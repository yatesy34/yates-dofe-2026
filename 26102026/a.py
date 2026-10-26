# 26/10/26 w3schools python: 
# lists, tuples, sets, dictionaries
# end at dictionaries: change items
# 2hrs

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 

thislist.append('ajwdoaiwjd')
print(thislist) 
thislist.insert(1, "orange")
print(thislist) 
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thislist.remove("banana")
print(thislist)
thislist.pop(1)
print(thislist)
del thislist[1]
print(thislist)
thislist.clear()
print(thislist)
thislist = ["apple", "banana", "cherry"]
for i in thislist:
  print(i)
for i in range(len(thislist)):
  print(i)
[print(i) for i in thislist]
newlist = []

for x in thislist:
  if "a" in x:
    newlist.append(x)
print(newlist)
newlist = [x for x in thislist if 'a' in x]
print(newlist)
# newlist = [expression for item in iterable if condition == True]
newlist = [x for x in range(10)] 
print(newlist)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
newlist = list(newlist)
print(newlist)
mylist = thislist[:]
print(mylist)

# Create a list
colors = ['red', 'green', 'blue']
# Print the first item
print(colors[0])
# Change the second item to "yellow"
colors[1] = 'yellow'
# Add "purple" to the end
colors.append('purple')
# Remove "red"
colors.remove('red')
# Print the list
print(colors)

# --------
#  Tuples
# --------

thistuple = 'apple', 'banana', 'cherry'
print(thistuple)

# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) 
tuple1 = ("apple", "banana", "cherry", 1, 5, 7, 9, 3)
print(tuple1)
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
mylist = list(thistuple)
mylist[1] = 'wdaoidwja'
newtuple = tuple(mylist)
print(newtuple)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry", "apple")

(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)

print(fruits.index('apple', 1))

# Create the tuple
fruits = 'apple', 'banana', 'cherry'
# Print the second item
print(fruits[1])
# Print the number of items
print(len(fruits))
# Unpack the tuple
(a, b, c) = fruits
# Print b
print(b)

# ------
#  Sets
# ------

# unordered unchangeable, unindexed
# can still add or remove items

thisset = {'apple', 'banana', 'cherry', 'apple', True, 1, False, 0}
print(thisset)
set1 = {"abc", 34, True, 40, "male"} 
print(type(thisset))
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 
# thisset = {"apple", "banana", "cherry"}

# for x in range(len(thisset)):
#   print(thisset[x]) 
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) 
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) 
thisset.remove("banana")
print(thisset) 
thisset.discard("baanana")
print(thisset) 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
set3 = set1 | set2
print(set3) 
set1.update(set2)
print(set1) 
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)
set3 = set1 & set2
print(set3) 
set1.intersection_update(set2)
#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
print(set1) 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
set3 = set1 - set2
print(set3) 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
set3 = set1 ^ set2
print(set3) 
set1.symmetric_difference_update(set2)
print(set1) 
x = frozenset({"apple", "banana", "cherry"}) # cant add or remove anything
print(x)
print(type(x))

# Create the set
colors = {'red', 'green', 'blue'}
# Print the set
print(colors)
# Add "yellow"
colors.add('yellow')
# Remove "green"
colors.discard('green')
# Print the number of items
print(len(colors))

# --------------
#  Dictionaries
# --------------

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict['brand'])
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) 
print(len(thisdict))
# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)
x = thisdict.get("model")
print(x)
x = thisdict.keys() 
print(x)
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change 
x = thisdict.values() 
print(x)
x = thisdict.items() 
print(x)
if "model" in thisdict:
  print("awobabobob")
identifier = {
  "key": "value"
}