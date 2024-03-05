# Exercise 19
# Write a Python program that calculates the sum S=1+2+3+4+….+ N. where N entered on the keyboard by the user.  Using the for loop.  


N=int(input("Enter the number for N : "))
S=0
for i in range(1,N+1):
    S=S+i
print(f"The sum of 1 to N is {S}")