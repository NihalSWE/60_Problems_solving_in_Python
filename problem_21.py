# Exercise 21
# Write a Python program that displays the multiplication table of an integer entered by the user, using the for loop.  



N=int(input("Enter the value of N: "))

for i in range(1,11):
    print(f"{N} * {i} = {N*i}")

