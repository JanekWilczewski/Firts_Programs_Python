from math import *

a = int(input("Provide a: "))
b = int(input("Provide b: "))
c = int(input("Provide c: "))

delta = b**2 - 4 * (a * c)

if delta < 0:
    print("No solution")

else:
    if delta > 0:
        x1 = -b - sqrt(delta) / (2 * a)
        x2 = -b + sqrt(delta) / (2 * a)

        print("x1=", x1)
        print("x2=", x2)

    else:
        x0 = -b / (2 * a)
        print("x0=", x0)






