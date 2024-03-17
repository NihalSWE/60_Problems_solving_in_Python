# Exercise 41
# Create a Python program that creates and initializes an array, then display all unique elements of that array
# Idea: use a frequency table.

arr=[]
uniq=[]
n=int(input("Enter the limit: "))
for i in range(1,n+1):
    ele=int(input(f"Enter element {i}: "))
    arr.append(ele)
    if ele not in uniq:
        uniq.append(ele)
print(f"The entered array is: {arr}")
print(f"The uniq element is :{uniq} ")