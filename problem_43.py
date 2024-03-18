# Exercise 43
# Create a Python program that creates and initializes an array, then remove duplicate elements in that array. 
arr=[]
new_arr=[]
n=int(input("Enter limit: "))
for i in range (1,n+1):
    ele=int(input(f"Enter {i} element: "))
    arr.append(ele)
    if ele not in  new_arr:
        new_arr.append(ele)
print(f"Given array is: {arr}")
print(f"New array without repetition is: {new_arr}\n")

    