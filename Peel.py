# Hello, I have created a project that aims to identify people after a peel.

# Asking peel
peel = input('Please provide your peel: ')

# Defines a list with peel
list = []
list.extend(peel)


# Defines month, day, year and gender in sequence
month = list[2] + list[3]
year = list[0] + list[1]
sex = list[9]
day = list[4] + list[5]

# Adds months to the list
list2 = ['January', 'February', 'March',
'April', 'May', 'June', 'July', 'August',
'September', 'October', 'November', 'December']

# Exchange items on the list for numbers
sex1 = int(sex)
month1 = int(month)
year1 = int(year)
day1 = int(day)


# year2 - Date of birth before 2000
# age - Current age (Born before 2000)
# year3 - Date of birth after 2000
# age1 - Current age (Born after 2000)

year2 = year1 + 1900
age = 2020 - year2
year3 = year1 + 2000

# Checks whether the person was born before 2000 or later and calculates the current age
if month1 <= 12:
    year2 = year1 + 1900
    age = 2020 - year2

# Assigns a specific number to the specified month
    if month1 == 1:
        print('You was born in', year2, 'in', day1, (list2[0]))
    elif month1 == 2:
        print('You was born in', year2, 'in', day1, (list2[1]))
    elif month1 == 3:
        print('You was born in', year2, 'in', day1, (list2[2]))
    elif month1 == 4:
        print('You was born in', year2, 'in', day1, (list2[3]))
    elif month1 == 5:
        print('You was born in', year2, 'in', day1, (list2[4]))
    elif month1 == 6:
        print('You was born in', year2, 'in', day1, (list2[5]))
    elif month1 == 7:
        print('You was born in', year2, 'in', day1, (list2[6]))
    elif month1 == 8:
        print('You was born in', year2, 'in', day1, (list2[7]))
    elif month1 == 9:
        print('You was born in', year2, 'in', day1, (list2[8]))
    elif month1 == 10:
        print('You was born in', year2, 'in', day1, (list2[9]))
    elif month1 == 11:
        print('You was born in', year2, 'in', day1, (list2[10]))
    elif month1 == 12:
        print('You was born in', year2, 'in', day1, (list2[11]))

    # Checks whether a person is a woman or a man
    if sex1 % 2 == 0:
        print('You have', age, "year's old and you are woman")
    else:
        print('You have', age, "year's old and you are man")

    year3 = year1 + 2000
    age1 = 2020 - year3

# Calculates the same for those born above 2000
else:
    if month1 > 12:
         year3 = year1 + 2000
         age1 = 2020 - year3
         if month1 % 20 == 1:
             print('You was born in', year3, 'in', day1, (list2[0]))
         elif month1 % 20 == 2:
             print('You was born in', year3, 'in', day1, (list2[1]))
         elif month1 % 20 == 3:
             print('You was born in', year3, 'in', day1, (list2[2]))
         elif month1 % 20 == 4:
             print('You was born in', year3, 'in', day1, (list2[3]))
         elif month1 % 20 == 5:
             print('You was born in', year3, 'in', day1, (list2[4]))
         elif month1 % 20 == 6:
             print('You was born in', year3, 'in', day1, (list2[5]))
         elif month1 % 20 == 7:
             print('You was born in', year3, 'in', day1, (list2[6]))
         elif month1 % 20 == 8:
             print('You was born in', year3, 'in', day1, (list2[7]))
         elif month1 % 20 == 9:
             print('You was born in', year3, 'in', day1, (list2[8]))
         elif month1 % 20 == 10:
             print('You was born in', year3, 'in', day1, (list2[9]))
         elif month1 % 20 == 11:
             print('You was born in', year3, 'in', day1, (list2[10]))
         elif month1 % 20 == 12:
             print('You was born in', year3, 'in', day1, (list2[11]))
         if sex1 % 2 == 0:
             print('You have', age1, "year's old and you are woman")
         else:
             print('You have', age1, "year's old and you are man")
