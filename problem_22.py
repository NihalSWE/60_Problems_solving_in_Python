# Exercise 22  **
# Write a Python program, enter two numbers from the user and find the greatest common divisor using the for loop.

m=int(input("Enter the first number: "))
n=int(input("Enter the second number: "))

if m<n:
    min=n
else:
    min=m

for i in range (1,min+1):
    if  m%i==0 and n%i==0:
        gcd=i
print(f"The common divisor of {m} and {n} is = {gcd}")

    