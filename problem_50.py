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


class Account:
    # Constructor to set the initial balance
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    # Method to get the current balance
    def getBalance(self):
        return self.balance
    
    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
    
    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    # Method to add interest to the account
    def add_Interest(self, interest_rate):
        self.balance *= (1 + interest_rate)

# Get initial balance from the user
initial_balance = float(input("Enter the initial balance for the account: "))
account = Account(initial_balance)  # Create an account with the user's balance

# Main loop for user interaction
while True:
    print("\nAccount Menu:")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Add interest")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        # Option 1: Show current balance
        print(f"Your current balance is: ${account.getBalance():.2f}")
    
    elif choice == '2':
        # Option 2: Deposit money
        amount = float(input("Enter the amount to deposit: $"))
        account.deposit(amount)
        print(f"Deposited ${amount:.2f}. Your new balance is: ${account.getBalance():.2f}")
    
    elif choice == '3':
        # Option 3: Withdraw money
        amount = float(input("Enter the amount to withdraw: $"))
        account.withdraw(amount)
        print(f"Your new balance is: ${account.getBalance():.2f}")
    
    elif choice == '4':
        # Option 4: Add interest
        interest_rate = float(input("Enter the interest rate (e.g., 0.05 for 5%): "))
        account.add_Interest(interest_rate)
        print(f"Interest added. Your new balance is: ${account.getBalance():.2f}")
    
    elif choice == '5':
        # Option 5: Exit
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid option, please choose a number between 1 and 5.")

