a = input("Do you provide weight and growth in kg and m? yes/no: ")

if a == "yes":
# Asking weight and growth in kg and meaters    
    weight = float(input("Enter your weight(kg): "))
    growth = float(input("Enter your growth(m): "))
# Calculate BMI for kg and m    
    BMI = weight/growth**2

# Asking weight and growth in lb and inches
else:
    weight = float(input("Enter your weight(lb): "))
    growth = float(input("Enter your growth(in): "))
 # Calculate BMI for lb and in
    BMI = weight / (growth ** 2) * 703

# Range checking
# Checks if BMI is less than 16
if BMI < 16:         
    print("Starvation")

# Checks if BMI is bigger than 16 and less than 17
elif BMI >= 16 and BMI < 17:
    print("Emaciation")

# Checks if BMI is bigger than 17 and less than 18.49
elif BMI >= 17 and BMI < 18.49:
    print("Underweight")

# Checks if BMI is bigger than 18.5 and less than 25
elif BMI >= 18.5 and BMI < 25:
    print("Optimum")

# Checks if BMI is bigger than 25 and less than 30
elif BMI >= 25 and BMI < 30:
    print("Overweight")

# Checks if BMI is bigger than 30 and less than 35
elif BMI >= 30 and BMI < 35:
    print("1st degree obesity")

# Checks if BMI is bigger than 35 and less than 40
elif BMI >= 35 and BMI < 40:
    print("Second degree obesity (major)")

# Checks if BMI is bigger than 40
elif BMI >= 40:
    print("III degree obesity (morbid)")


