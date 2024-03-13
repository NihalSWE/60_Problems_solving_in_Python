# Exercise 38
# Create a Python program that creates and initializes an array, 
# then inserts an element at the specified position in that array (from 0 to N-1).
# To insert a new element into the array, move the elements from the given insertion position to one position to the right.


arr=[]
n=int(input("Enter limit: "))
for i in range(n):
    ele=int(input(f"Enter Element {i}:"))
    arr.append(ele)
print(f"Original Array is :{arr}")
pos=int(input("Enter Position where you want to insert the element:"))
value=int(input("Enter Value to be inserted:"))
if pos<0 or pos>len(arr):
    print("Invalid Position")
    exit()

arr.insert(pos,value)
print(f"Array after Insertion:{arr}")
