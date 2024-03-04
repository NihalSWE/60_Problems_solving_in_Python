# Exercise 11
# The photocopy center charges 0.25 tk for the first 10 photocopies, 0.20 tk for the next twenty and 0.10 tk for more than twenty. 
# Write a Python program that asks the user to enter the number of photocopies made and displays the corresponding invoice. 

num_of_copys=int(input("Enter the number of copies: "))
if  num_of_copys<=0 :
    print("Invalid input")
elif  num_of_copys<=10 and num_of_copys>0:
    price_per_copy = 0.25
    total_price=price_per_copy*num_of_copys
    print(f"The cost for {num_of_copys} copies is {total_price}tk")
elif  num_of_copys>10 and num_of_copys <=20:
    price_per_copy = 0.20
    total_price=price_per_copy*num_of_copys
    print(f"The cost for {num_of_copys} copies is {total_price}tk")
elif  num_of_copys > 20:
    price_per_copy = 0.10
    total_price=price_per_copy*num_of_copys
    print(f"The cost for {num_of_copys} copies is {total_price}tk")
else:
    print("Error!")
