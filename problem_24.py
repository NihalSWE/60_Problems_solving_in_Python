# Exercise 24
# Write a Python program  to input a number and calculate its factorial using the for loop.

# The factorial of a number "n" is the product of all positive integers less than or equal to n. It is noted n!.
# For example, factorial of 5!= 1*2*3*4*5= 120.

num  = int(input("Enter a positive integer: "))
fac=1

for i in range(1,num+1):
    fac = fac * i
print("Factorial of", num,"is", fac)
