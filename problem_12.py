# Exercise 12
# Write a Python program which asks for the age of a child and provides information on its category, 
# knowing that the categories are as follows: 
# "6 to 7 year old chick"   
# "8 to 9 year old ward"   
# "minimum of 10 to 11 years old "  
# "junior after 12 years". 

child_age=int(input("Enter your child age: "))

if child_age>=6 and  child_age<=7:
    print(f"Your child is a chick")
elif  child_age>=8 and child_age<=9:
    print(f"Your child is a ward.")
elif  child_age>=10 and child_age<=11:
    print(f"Your child is minimal")
elif  child_age>=12:
    print(f"Your child is junior" )
else:
    print("Invalid input")