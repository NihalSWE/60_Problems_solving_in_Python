# Exercise 30
# Write a Python program to grab the user's number and check whether the number is palindrome or not, using a loop.

num=int(input("Enter a number: "))

num_str=''.join(reversed(str(num)))
is_plindrome=True


for i in range(len(num_str)):
    if  num_str[i] != str(num)[i]:
        is_plindrome=False
        break

if  is_plindrome:
    print (f"The entered number {num} is palindrome")
else:
    print(f"The entered number {num} is not palindrome")

