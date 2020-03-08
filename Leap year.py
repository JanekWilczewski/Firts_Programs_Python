year = int(input("Provide year: "))


divisible4 = year / 4

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")

else:
    print("Normal year")