# Exercise 13 
# Write a Python program to display the month in letters according to the number entered on the keyboard. 
# (If the user types 1 the program displays January, if 2 displays February, if 3 displays March...). 

month=int(input("Enter  the number of the month: "))

if  month == 1 :
    print(f"The month is {month} - January")
elif month  == 2 :
    print(f"The month is {month} - February")
elif month == 3:
    print(f"The month is {month} - March")
elif month ==4 :
    print(f"The month is {month} - April")
elif month == 5:
    print(f"The month is {month} - May")
elif month == 6:
    print(f"The month is {month} - June")
elif month == 7:
    print(f"The month is {month} - July")
elif month == 8:
    print(f"The month is {month} - August")
elif month == 9:
    print(f"The month  is {month} - September")
elif month == 10:
    print(f"The month is {month} - October")
elif month == 11:
    print(f"The month is {month} - November")
elif month == 12:
    print(f"The month is {month} - December")
else:
    print("Invalid Input")
