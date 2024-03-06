# Exercise 32
# Write a Python program to declare an array, then user-enter its elements and display all negative elements.


arry=[]
neg_array=[]
num=int(input("Enter the limit: "))

for i in range(1, num+1):
    ele = int(input(f"Enter element {i}:"))
    arry.append(ele)
    if  ele < 0:
        neg_array.append(ele)
print(f"The entered array is :{arry}")
print(f"Negative  elements are : {neg_array}")
