# Exercise 42
# Create a Python program that creates and initializes an array, then count duplicate elements in that array.



arr=[]

n=int(input("Enter limit: "))
for i in range (1,n+1):
    ele=int(input("Enter element "+str(i)+":"))
    arr.append(ele)

print(f"The given array is {arr}")

count={}
for ele in arr:
    if  ele  in count:
        count[ele]+=1
    else:
        count[ele]=1
same=0
for  i,value in count.items():
    if value>1:
        same+=1
print(f"{same} duplicate elements in the array.")
