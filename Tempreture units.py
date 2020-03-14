#Hi! I have created a script that converts temperature units

#Asks for unit
unit = input("Select your units; Celsius - c, Fahrenheit - f, Calvin - k: ")

#Calculates units relative to Celsius
if unit == "c":
    c = int(input("Enter temperature in Celsius: "))
    f = (c * 1.8) + 32
    k = c + 273.15
    print(c,"C = ",f,"F")
    print(c,"C =",k,"K" )
#Calculates units relative to Fahrenheit
elif unit == "f":
    f = int(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) / 1.8
    k = (f + 459.67) * (5/9)
    print(f, "F = ",c, "C")
    print(f, "F =",k, "K")

#Calculates units relative to Kelvin   
elif unit == "k":
    k = int(input("Enter temperature in calvin (Kelvin): "))
    c = k - 273.15
    f = (k * 1.8) - 459.67
    print(k, "K = ", c, "C")
    print(k, "K =", f, "F")

else:
    print("Wrong unit")



