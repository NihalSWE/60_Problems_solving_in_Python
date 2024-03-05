# Exercise 25
# Write a Python program to display all odd numbers from 1 to n using for and while loop.

n=int(input("Enter the value of n: "))
print("Odd Numbers from 1 to",n,"are")

ODD=[]


#  Using For Loop
for i in range(1,n+1):
    if i%2 !=0:
        ODD.append(i)
print(ODD)


# Using While Loop
j=1
while j<=n:
    if  j%2!=0:
        ODD.append(j)
    j+=1
print(ODD)