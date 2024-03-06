# Exercise 27
# Write a Python program to input a number from the user and find the first and last digit of a number using a loop.

num=int(input("Enter a number: "))

num1=str(num)

first_digit=None
last_digit=None

for i in num1:
    current_digit=int(i)
    if first_digit is None:
        first_digit = int(current_digit)
        print(f"{first_digit} is the first digit of {num}")
last_digit = int(current_digit)
print(f"{last_digit} is the last digit of {num}")


