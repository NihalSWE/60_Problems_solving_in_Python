# Exercise 34
# Write a Python program to declare an array, then grab its elements from the user 
# and find the maximum and minimum elements in the array.


arr=[]

n=int(input("Enter the limit: "))
first_ele=max=min=int(input("Enter first element: "))
for i in range(2,n+1): # If you can get max and min directly the you use(1,n+1) instead of (2,n+1)
    ele=int(input(f"Enter {i} element :"))
    arr.append(ele)
    if max < ele:
        max=ele 
    if min > ele:
        min=ele
      
# max=max(arr)
# min=min(arr)  #directly

arr.insert(0, first_ele)

print(f"The array : {arr}")
print(f"{max} is the  largest of {arr}")
print(f"{min} is the smallest of {arr}")


      