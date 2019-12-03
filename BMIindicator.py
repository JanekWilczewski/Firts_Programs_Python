a = input("Do you provide weight and growth in kg and m? yes/no: ")

if a == "yes":
    weight = float(input("Enter your weight(kg): "))
    growth = float(input("Enter your growth(m): "))
    BMI = weight/growth**2

else:
    weight = float(input("Enter your weight(lb): "))
    growth = float(input("Enter your growth(in): "))
    BMI = weight / (growth ** 2) * 703


if BMI < 16:
    print("starvation")

elif BMI >= 16 and BMI < 17:
    print("emaciation")

elif BMI >= 17 and BMI < 18.49:
    print("underweight")

elif BMI >= 18.5 and BMI < 25:
    print("optimum")

elif BMI >= 25 and BMI < 30:
    print("overweight")

elif BMI >= 30 and BMI < 35:
    print("1st degree obesity")

elif BMI >= 35 and BMI < 40:
    print("second degree obesity (major)")

elif BMI >= 40:
    print("III degree obesity (morbid)")


