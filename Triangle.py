import math

a = int(input("Provide a: "))
b = int(input("Provide b: "))
c = int(input("Provide c: "))

# Adds to lists
list = []
list.append (a)
list.append (b)
list.append (c)


if a < b + c and b < a + c and c < b + a:
    print("The triangle exists")
    print("Circuit is:", (a + b + c))
else:
    print("The triangle does not exist")

if a ** 2 + b ** 2 == c ** 2:
    print("Triangle rectangular")
else:
    print("Triangle not rectangular")

if a < b + c and b < a + c and c < b + a:
   F = (a + b + c) / 0.5

   F = math.sqrt (F * (F - a) * (F - b) * (F - c))
print("Field is:", F)


