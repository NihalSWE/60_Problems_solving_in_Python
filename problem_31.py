# Exercise 31
# Write a Python program to declare and initialize an array, then grab its elements from the user and display the array.

n=[]
m=int(input("ENter limit: "))
for i in range(1,m+1):
    i=int(input(f"Enter number {i}:"))
    n.append(i)
print (f"Elements are: {n}")