# Exercise 57: Arithmetic calculation
# 1) Create a Calculation class with a default constructor (without parameters) allowing to perform different calculations on integers.
# 2) Create within the Calculation class a method named Factorielle() which allows to calculate the factorial of an integer. Test the method by instantiating it on the class.
# 3) Create within the Calculation class a method named Somme() allowing to calculate the sum of the first n integers: 1 + 2 + 3 + .. + n. Test the method.
# 4) Create within the Calculation class a method named testPrim() allowing to test the primality of a given integer. Test the method.
# 5) Create within the Calculation class a method named testPrims() allowing to test if two numbers are prime to each other.
# 6) Create a method tableMult() that creates and displays the multiplication table of a given integer. Then create a method allTablesMult() to display all the multiplication tables of the integers 1, 2, 3, ..., 9.
# 7) Create a method listDiv() that retrieves all the divisors of a given integer on a list Ldiv. Create another method listDivPrim() that retrieves all the prime divisors of a given integer.

import math

class Calculation:
    def __init__(self):
        pass

    # def Factorielle(self):
    #     n=int(input("Enter the number for Factorial:"))
    #     if n<0:
    #         print("Factorial is not defined for negative numbers")
    #         return
        
    #     factorial=1
    #     if n==0:
    #         print("The factorial of 0 is 1")
    #     else:   
    #         for i in range(1,n+1):
    #             factorial *= i
    #         print ("The factorial of",n,"is",factorial)    

    # def Somme(self, n):
    #     return (f"Somme of {n} is : {n * (n + 1) // 2}")  
    
    def testPrim(self,n):
        # n=int(input("Enter the number you want to check: "))
        if n <= 1:
            # print(f"{n} is not a prime number.")
            return False
        for i in range (2,int(n**0.5)+1):
            if n%i == 0:
                # print(f"{n} is not a prime number")
                return False
            
        # print(f"{n} is  a prime number")
        return True
        
    # def testPrims(self):
    #     n1 = int(input("Enter the first number: "))
    #     n2 = int(input("Enter the second number: "))
    #     # Check if both numbers are prime
    #     if self.testPrim(n1) and self.testPrim(n2):
    #         print(f"{n1} and {n2} are both prime numbers.")
    #     else:
    #         print(f"One or both numbers are not prime.")
            
    #     # Check if n1 and n2 are coprime (gcd = 1)
    #     if math.gcd(n1, n2) == 1:
    #         print(f"{n1} and {n2} are coprime (i.e., prime to each other).")
    #     else:
    #         print(f"{n1} and {n2} are not coprime.")

    # def tableMult(self):
    #     n = int(input("Enter a number you want table: "))
    #     for i in range(1, 11):
    #         print(f"{n} x {i} = {n * i}")

    # def allTablesMult(self):
    #     for i in range(1, 11):
    #         print(f"\nTable of {i}")
            
    #         for j in range(1, 11):
    #             print(f"{i} x {j} = {i * j}")
               

    def listDiv(self,n):
        # n = int(input("Enter a number you want to find divisors: "))
        divisior=[]
        for i in range (1,n+1):
            if n%i == 0:
                divisior.append(i)
        # print(f"The divisiors of {n} are: {divisior}")
        return divisior  # Return the list of divisors

    def listDivPrim(self):
        n = int(input("Enter a number you want to find divisors: "))
        divisors = self.listDiv(n)
        prime_divisors = [i for i in divisors if self.testPrim(i)]  # Filter only prime divisors
        print(f"The prime divisors of {n} are: {prime_divisors}")


t1=Calculation()
# t1.Factorielle()
# print(t1.Somme(5))
# t1.testPrim(7)
# t1.testPrims()  
# t1.tableMult()
# t1.allTablesMult()  
# t1.listDiv()
t1.listDivPrim()