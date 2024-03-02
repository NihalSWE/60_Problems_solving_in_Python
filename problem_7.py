# Exercise 7                               
# Write a Python program that asks the user for two numbers m and n and then informs 
# them whether the product of these two numbers is positive or negative. 
# We include in the program the case where the product may be zero. 

m=int(input("Enter first number: "))
n=int(input("Enter second number: "))
product=m*n
if product>0:
    print(f"The product is positive.which is {product}")
elif product == 0:
    print(f"The product is zero. {product}")
else:
    print(f"The product is negative. which is {product}")