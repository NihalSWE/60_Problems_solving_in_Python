# Exercise 50  : Account class 
# Write a program  in Python  that simulates the management of a simple bank account. The account is created with an initial balance. It is possible to deposit and withdraw funds, add interest, and know the current balance. This should be implemented in a class named Account that includes:


# 1) A default constructor that sets the initial balance to zero.
# 2) A constructor that accepts an initial balance as a parameter.
# 3) A getBalance function that returns the current balance.
# 4) A deposit method to deposit a specified amount.
# 5) A withdraw method to withdraw a specified amount.
# 6) An add_Interest method to add interest to the account.
# The add_Interest method takes the interest rate as a parameter and changes the account balance to balance * (1 + interest rate).




class Account:
    def __init__(self, balance=0):
        self.balance = balance
    
    def get_balance(self):
        return self.balance
    
    def deposite(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            return self.balance

    def Add_interest(self,interest_rate):
        self.balance = self.balance * (1 + interest_rate)



my_account=Account(100)
print(my_account.get_balance())  # Output: 100
my_account.deposite(50)
print(my_account.get_balance())  # Output: 150
my_account.withdraw(30)
print(my_account.get_balance()) # Output: 130
my_account.Add_interest(0.05)
print(my_account.get_balance())  # Output: 126.0

