# Exercise 39
# Create a Python program that creates and initializes an array, then delete an element 
# from that array at the specified position (0 to N-1).To remove an element from the array, move the elements immediately 
# after the given position to a position to the left and reduce the size of the array.

arr=[]
n=int(input("Enter limit : "))
for i in range(0,n):
    ele=int(input(f"Enter number {i}:"))
    arr.append(ele)

print(f"Original Array is {arr}")
pos=int(input('Enter the position you want to delete : '))
if pos<0 or pos>=len(arr):
    print('Invalid Position')
else:
    del arr[pos]

print(f"Array after delete {arr}")
