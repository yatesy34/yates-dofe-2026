# 13/10/26 w3schools
# 1 hour
# python lists, string methods,
# booleans, operators
a = "The quick brown fox jumped over the lazy dog"
print(a.casefold())
print(a.count("a"))
print(a.encode())
print(a.find("uick"))
print(a.isascii())
# Create the variable
txt = "Hello, World!"
# Print characters from index 2 to 5
print(txt[2:5])
# Print in upper case
print(txt.upper())
# Create the name variable
name = "Python"
# Print using an f-string
print(f"I love {name}")
print(bool(15))
x = 5
print(1 < x < 10)
print(1 < x and x < 10)
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
print(6 & 3) #and
print(6 | 3) #or
print(6 ^ 3) #xor
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(len(thislist))
print(type(thislist))
print(thislist[-1])
print(thislist[1:3])
print("apple" in thislist)
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist.insert(2, "watermelon") # insert after 2nd index
print(thislist)
