# Exercise 16
# Write a Python program to calculate the sum S=1+2+3+...+ N, where N entered by the user. Using the while loop.  

N=int(input("Enter the number you want  for N: "))

i=1
s=0
while i<=N:
    s=s+i
    i+=1
print(f"the sum of 1 to N is: {s}")