# Exercise 5      
# Write a Python program that displays the largest of three integers entered on the keyboard. 

m=int(input("Enter first integer: "))
n=int(input("Enter second integer: "))
l=int(input("Enter third integer: "))

if m>n and m>l :
    print (f"{m} is the largest number " )
elif n>l:
    print (f"{n} is the largest number")
else:
    print(f"{l} is the largest number")