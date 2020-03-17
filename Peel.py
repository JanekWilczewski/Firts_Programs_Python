# Hello, I have created a script that aims to identify people after a peel.

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
    month3 = month1 - 1

    print('You was born in', year2, 'in', day1, (list2[month3]))

    # Checks whether a person is a woman or a man
    if sex1 % 2 == 0:
        print('You have', age, "year's old and you are woman")
    else:
        print('You have', age, "year's old and you are man")

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
         month4 = month1 - 21
    print('You was born in', year3, 'in', day1, (list2[month4]))
    if sex1 % 2 == 0:
        print('You have', age1, "year's old and you are woman")
    else:
        print('You have', age1, "year's old and you are man")
