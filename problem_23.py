# Exercise 23
# Write a Python program to enter a number and check whether the number is perfect or not.
# A perfect number is a positive integer that is equal to the sum of its appropriate positive divisors.
# For example: 6 is the first perfect number
# The proper divisors of 6 are 1, 2, 3.
# Sum of its strict divisors = 1 + 2 + 3 = 6.
# Therefore, 6 is a perfect number. 

num=int(input("ENter a number: "))
sum=0

for  i in range(1, num):
    if num % i == 0:
        sum+=i
if sum==num:
    print(f"{num} is a Perfect Number")
else:
    print(f"{num} is not a Perfect Number")