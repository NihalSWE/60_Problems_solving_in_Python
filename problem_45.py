# Exercise 45
# Write a Python program that calculates the sum:
# S = 1¹ +2² + 3³ +.....+ n^n

sum=0
n=int(input("Enter the value of n: "))
for i in range(1,n+1):
    sum += (i**i)
print(f"The sum is {sum}")