# Exercise 37
# Write a Python program to declare two arrays, then enter the elements of the 
# user's first array and copy all its elements into the second array.

arr1=[]
ar2=[]
n = int(input("Enter the number of elements in arr1: "))

for i in  range(1,n+1):
    ele=int(input(f"Enter {i} elements :"))
    arr1.append(ele)
arr2=arr1.copy()
# arr2=arr1[:]
print(f"Elements in arr1 are: {arr1}")
print(f"Copy elements of  arr1 in arr2: {arr2} ")