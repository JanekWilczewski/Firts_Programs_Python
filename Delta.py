#Hello, I created a script that calculates the delta with its zero places

from math import *

#Gets numbers from the user
a = int(input("Provide a: "))
b = int(input("Provide b: "))
c = int(input("Provide c: "))

#Calculates a delta from the formula
delta = b**2 - 4 * (a * c)

if delta < 0:
    print("No solution")

else:
    if delta > 0:
#Calculates x1 and x2     
        x1 = -b - sqrt(delta) / (2 * a)
        x2 = -b + sqrt(delta) / (2 * a)

        print("x1=", x1)
        print("x2=", x2)

    else:
        x0 = -b / (2 * a)
        print("x0=", x0)






