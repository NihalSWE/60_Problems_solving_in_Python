# Exercise 36
# Write a Python program to declare an array, then grab its elements from the user and
# count the number of even and odd elements in this array.

arr=[]
even_ele=0
odd_ele=0
n=int(input("ENter limit of the array: "))
first_ele=int(input("Enter first element: "))
for i in range(2,n+1):
    ele=int(input(f"Enter {i} element: "))
    arr.append(ele)


arr.insert(0,first_ele)
for i in arr:
    if i%2==0:
        even_ele+=1
    else:
        odd_ele+=1
        


print(f"The entered array is :{arr}")
print(f"The number of even elements  are:{even_ele}")
print(f"The number of odd elements are:{odd_ele}")