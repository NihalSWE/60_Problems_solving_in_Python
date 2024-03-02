# Exercise 4      

# Write a Python program that displays whether an integer entered on the keyboard is even or odd. 

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")