# Exercise 28
# Write a Python program that reverses the digits of an integer N entered by the user. 
# for example N=35672 the displayed result must be 27653. 

num=int(input("Enter a number: "))

R=''.join(reversed(str(num)))   
N=int(R)                        



print(f"Reverse of {num} is - {N}")


