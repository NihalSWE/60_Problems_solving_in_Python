# Exercise 35
# Write a Python program to declare an array, then grab its elements from user and find the largest and second largest element in this array.

arr=[]
n=int(input("Enter the limit: "))
first_ele=max1=max2=int(input("ENter first element: "))
for i in range(2,n+1):
    ele=int(input(f"Enter {i} element :"))
    arr.append(ele)
    if ele>max1:
        max2=max1
        max1=ele
    if ele>max2 and ele!=max1:
        max2=ele
    
arr.insert(0,first_ele)
print(f"The array is :{arr}")
print(f"First Maximum value is:{max1}")
print(f"Second maximum value is:{max2}")

      