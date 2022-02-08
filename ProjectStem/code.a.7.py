def leap_year(y):
    if(y % 400 == 0):
        return 1
    elif(y % 100 == 0):
        return 0
    elif(y % 4 == 0):
        return 1
    else:
        return 0
    return y

def number_of_days(m,y):
    y = leap_year(y)
    if(m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        return 31
    elif(m == 4 or m == 6 or m == 9 or m == 11):
        return 30
    elif(m == 2 and y == 1):
        return 29
    elif(m == 2 and y == 0):
        return 28

def days_left(d,m,y):
    sum = 0
    for i in range(m, 13):
       sum = sum + number_of_days(m, y)
       m = m + 1
    return sum - d



print("Please enter a date")

d = int(input("Day: "))
if(d < 1 or d > 31):
    print("Make sure day is between 1 or 31")
    end=" "

m = int(input("Month: "))
if (m < 1 or m > 12):
    print("Make sure month is between 1 or 12")
    end=" "

y = int(input("Year: "))
if (y < 0):
    print("Can't be less than 0")
    end=" "

print("Menu:\n1) Calculate the number of days in the given month.\n2) Calculate the number of days left in the given year.")

monOrYear = int(input(""))

if (monOrYear == 1):
        print(number_of_days(m, y))
elif (monOrYear == 2):
        print(days_left(d, m, y))
else:
    print("Invalid selection pick 1 or 2")
