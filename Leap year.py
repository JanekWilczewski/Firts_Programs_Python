#Hello!, I created a script that checks if a given year is leap or not

#Asks for a year
year = int(input("Provide year: "))

#Calculates when it is leap
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")

else:
    print("Normal year")
