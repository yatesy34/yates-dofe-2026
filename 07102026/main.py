# 07/10/26
# w3schools python: start -> strings
# 1h

from operator import length_hint

x=12931
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a[1])

for i in "bananas":
  print(i)

if "Ipsum" not in a:
    print("iawdadwa")

print(a[:5])

print(a[-5:-2])
print(a.upper())
c = "     awdadw "
print(c.strip())
print(c.replace("x", "b"))
print(a.split(" "))
print(f"awdawd {x}")
txt = f"The price is {x:.2f} dollars"
print(txt)
print("We are the so-\called \"Vikings\" from the north.")