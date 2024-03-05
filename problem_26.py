# Exercise 26
# Write a Python program to enter a number from the user and count the number of digits in the given integer using a loop.


num = int(input("Enter a number: "))
m=0
while  num > 0 :
    num = num // 10
    m+=1
print(m)

