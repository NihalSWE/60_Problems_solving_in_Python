# Exercise 3
# Write a Python program that allows you to exchange the contents of two integers
# A and B entered by the user. and display these integers after the exchange.   

def exchange_integers():
    A=int(input("Enter first integer: "))
    B=int(input("Enter second integer: "))
    print("\nBefore Exchange:")
    print("First Integer =",A)
    print("Second Integer =",B)
    temp=A
    A=B
    B=temp
    print("\nAfter Exchange:")
    print("First Integer =",A)
    print("Second Integer =",B)
    
exchange_integers()
    
