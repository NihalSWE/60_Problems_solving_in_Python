# Exercise 44  

# Create a Python program that creates and initializes an array, then invert that array without using an additional array.

arr=[]
n=int(input("Enter limit: "))
for i in range(1,n+1):
    ele=int(input(f"Enter {i} element: "))
    arr.append(ele)
length=len(arr)
for i in range(length//2):
    temp=arr[i]
    arr[i]=arr[length-i-1]
    arr[length-i-1]=temp
print(f"Reversed array is :{arr}")