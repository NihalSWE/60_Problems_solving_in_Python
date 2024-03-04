# Exercise 10
# A store offers these customers a 15% reduction for purchase amounts above 200 $. Write a Python program allowing 
# you to enter the total price excluding tax and calculate the amount including tax, taking into account the reduction and VAT=20%.  

Price_incl_tax = float(input("Enter the amount excluding tax:"))
Price_incl_tax = Price_incl_tax + Price_incl_tax*0.2
if Price_incl_tax > 200:
    Price_incl_tax = Price_incl_tax - Price_incl_tax*0.15
    print("the amount inclluding tax is: ",Price_incl_tax)  
else:
        print ("the amount including tax is: ", Price_incl_tax)