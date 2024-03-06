# Exercise 33
# Write a Python program to declare an array, then grab its elements from the user and find the sum of the array elements.

sum=0
limit=int(input(f"Enter the limit of array: "))

for i in  range(1,limit+1):
    ele=int(input(f"Enter element {i}:"))
    sum+=ele
print(f"The sum is :{sum}")