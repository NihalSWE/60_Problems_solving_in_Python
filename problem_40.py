# Exercise 40
# Create a Python program that creates and initializes an array, then finds the frequency of each element in that array.

arr=[]
n=int(input("Enter the limit of the array: "))
for i in range(1,n+1):
    ele=int(input(f"Enter {i} element: "))
    arr.append(ele)


print(f"The array {arr}")

frequency={}
for i in arr:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i] =1
for i , frequency[i] in frequency.items():

    print(f"{i} is stored {frequency[i]} times")
    


