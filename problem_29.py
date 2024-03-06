# Exercise 29
# Write a Python program to input a number and calculate the sum of its digits using the for loop.

num=int(input("Enter a number: "))
num1=str(num)
sum=0
for i in num1:
    digit=int(i)
    sum+=digit
print(f"The sum of {num} is {sum}")
